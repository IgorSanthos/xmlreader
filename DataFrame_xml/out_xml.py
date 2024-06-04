import pandas as pd
import xml.etree.ElementTree as ET
import glob
import os

# Função para converter DataFrame para XML e adicionar ao parent_element existente
def dataframe_to_xml(df, parent_element, row_element_name, sub_element_mapping=None, sub_sub_element_mapping=None, sub_sub_sub_element_mapping=None, ignore_columns=None):
    for _, row in df.iterrows():
        row_element = ET.SubElement(parent_element, row_element_name)    
        for col_name in df.columns:
            # Verifica se o valor é NaN ou espaço Pula a criação da tag se o valor for NaN
            if pd.isna(row[col_name]) or row[col_name] == '' or row[col_name] == ' ':
                continue
            # Pula a criação da tag se a coluna estiver na lista de colunas a serem ignoradas
            if ignore_columns and col_name in ignore_columns:
                continue 

            if sub_element_mapping and col_name in sub_element_mapping:
                sub_element_name = sub_element_mapping[col_name]
                sub_element = row_element.find(sub_element_name)
                if sub_element is None:
                    sub_element = ET.SubElement(row_element, sub_element_name)
                
                if sub_sub_element_mapping and col_name in sub_sub_element_mapping:
                    sub_sub_element_name = sub_sub_element_mapping[col_name]
                    sub_sub_element = sub_element.find(sub_sub_element_name)
                    if sub_sub_element is None:
                        sub_sub_element = ET.SubElement(sub_element, sub_sub_element_name)
                    
                    if sub_sub_sub_element_mapping and col_name in sub_sub_sub_element_mapping:
                        sub_sub_sub_element_name = sub_sub_sub_element_mapping[col_name]
                        sub_sub_sub_element = sub_sub_element.find(sub_sub_sub_element_name)
                        if sub_sub_sub_element is None:
                            sub_sub_sub_element = ET.SubElement(sub_sub_element, sub_sub_sub_element_name)
                        cell = ET.SubElement(sub_sub_sub_element, col_name)
                    else:
                        cell = ET.SubElement(sub_sub_element, col_name)
                else:
                    cell = ET.SubElement(sub_element, col_name)
                cell.text = str(row[col_name])
            else:
                cell = ET.SubElement(row_element, col_name)
                cell.text = str(row[col_name])


# Diretório contendo os arquivos Excel
excel_files = glob.glob(r'C:\Users\Igor\Desktop\XML EM UM DICIONARIO\DataFrame_xml/*.xlsx')

# Verificar se há arquivos Excel na pasta especificada
if not excel_files:
    print("Nenhum arquivo Excel encontrado.")
    exit()

# Criar uma pasta para salvar os arquivos XML
output_directory = r'C:\Users\Igor\Desktop\XML EM UM DICIONARIO\DataFrame_xml\XML_Output'
os.makedirs(output_directory, exist_ok=True)

# Ler os dados das planilhas
for excel_file in excel_files:
    df_idNFE = pd.read_excel(excel_file, sheet_name="Identificação NFE", dtype=str)
    df_emi = pd.read_excel(excel_file, sheet_name="Emitente", dtype=str)
    df_dest = pd.read_excel(excel_file, sheet_name="Destinatário", dtype=str)
    df_det = pd.read_excel(excel_file, sheet_name= "Itens", dtype=str)
    df_total = pd.read_excel(excel_file, sheet_name= "Total", dtype=str)
    df_transp = pd.read_excel(excel_file, sheet_name="Transportadora", dtype=str)
    df_cobranca = pd.read_excel(excel_file, sheet_name="Cobrança", dtype=str)
    df_pagamento = pd.read_excel(excel_file, sheet_name="Pagamento", dtype=str)
    df_info = pd.read_excel(excel_file, sheet_name="Inf. Adicional", dtype=str)
    #df_compras = pd.read_excel(excel_file, sheet_name="Compras", dtype=str)
    #df_respTec = pd.read_excel(excel_file, sheet_name="Resp. Tecnico", dtype=str)
    df_assinatura = pd.read_excel(excel_file, sheet_name="Assinatura", dtype=str)
    df_protocolo = pd.read_excel(excel_file, sheet_name="Protocolo", dtype=str)


#============================ SUB TAGS
# Aba Sub dos "Emitente"
    sub_emit = {"xLgr": "enderEmit", "nro": "enderEmit", "xCpl": "enderEmit", "xBairro": "enderEmit",
                "cMun": "enderEmit", "xMun": "enderEmit", "UF": "enderEmit", "CEP": "enderEmit",
                "cPais": "enderEmit", "xPais": "enderEmit", "fone": "enderEmit"}
                
# Aba Sub dos "Destino"
    sub_dest = {"xLgr": "enderDest", "nro": "enderDest", "xCpl": "enderDest", "xBairro": "enderDest",
                "cMun": "enderDest", "xMun": "enderDest", "UF": "enderDest", "CEP": "enderDest",
                "cPais": "enderDest", "xPais": "enderDest", "fone": "enderDest"}
                
# Aba Sub dos Itens
    sub_prod = {"NumItem": "prod","cProd":"prod", "cEAN":"prod", "xProd":"prod", "NCM":"prod", "CEST":"prod", "cBenef":"prod", "CFOP":"prod",
                "uCom":"prod", "qCom":"prod", "vUnCom":"prod", "vProd":"prod", "cEANTrib":"prod", "uTrib":"prod",
                "qTrib":"prod", "vUnTrib":"prod", "indTot":"prod"} 
                   
    # 1 - Impostos
    tag_impostos = {**sub_prod, "vTotTrib":"imposto", "orig":"imposto", "CSOSN":"imposto", "pCredSN":"imposto", "vCredICMSSN":"imposto","ICMS_CST":"imposto",
                    "ICMS_modBC":"imposto","ICMS_vBC":"imposto","ICMS_pICMS":"imposto","ICMS_vICMS":"imposto",
                    # PIS E COFINS
                    "PIS_CST":"imposto","PIS_vBC":"imposto","PIS_pPIS":"imposto","PIS_vPIS":"imposto",
                    "COFINS_CST":"imposto","COFINS_vBC":"imposto","COFINS_pCOFINS":"imposto","COFINS_vCOFINS":"imposto"}
    
    # 2 - Dentro de ICMS/PISCOFINS/IPI
    tagICMS = {"orig":"ICMS", "CSOSN":"ICMS", "pCredSN":"ICMS", "vCredICMSSN":"ICMS","ICMS_CST":"ICMS",
                "ICMS_modBC":"ICMS","ICMS_vBC":"ICMS","ICMS_pICMS":"ICMS","ICMS_vICMS":"ICMS",
                # PIS E COFINS
                "PIS_CST":"PIS","PIS_vBC":"PIS","PIS_pPIS":"PIS","PIS_vPIS":"PIS",
                "COFINS_CST":"COFINS","COFINS_vBC":"COFINS","COFINS_pCOFINS":"COFINS","COFINS_vCOFINS":"COFINS"}
    
    # 3 - TIPO DE ICMS
    tipodeICMS = "ICMS10"
    tipoPIS = "PISAliq"
    tipoCOFINS = "COFINAliq"
    tagICMSTipo = {"orig": tipodeICMS, "CSOSN":tipodeICMS, "pCredSN":tipodeICMS, "vCredICMSSN":tipodeICMS,"ICMS_CST":tipodeICMS,
                   "ICMS_modBC":tipodeICMS,"ICMS_vBC":tipodeICMS,"ICMS_pICMS":tipodeICMS,"ICMS_vICMS":tipodeICMS,
                   # PIS E COFINS
                   "PIS_CST":tipoPIS,"PIS_vBC":tipoPIS,"PIS_pPIS":tipoPIS,"PIS_vPIS":tipoPIS,
                   "COFINS_CST":tipoCOFINS,"COFINS_vBC":tipoCOFINS,"COFINS_pCOFINS":tipoCOFINS,"COFINS_vCOFINS":tipoCOFINS}
    
# Aba Sub do Total
    tag_ICMSTot = {"vBC": "ICMSTot","vICMS": "ICMSTot","vICMSDeson": "ICMSTot","vFCPUFDest": "ICMSTot", 
                   "vICMSUFDest": "ICMSTot","vICMSUFRemet": "ICMSTot","vFCP": "ICMSTot","vBCST": "ICMSTot",
                   "vST": "ICMSTot","vFCPST": "ICMSTot","vFCPSTRet": "ICMSTot","vProd": "ICMSTot","vFrete": "ICMSTot",
                   "vSeg": "ICMSTot","vDesc": "ICMSTot","vII": "ICMSTot","vIPI": "ICMSTot","vIPIDevol": "ICMSTot",
                   "vPIS": "ICMSTot","vCOFINS": "ICMSTot","vOutro": "ICMSTot","vNF": "ICMSTot","vTotTrib": "ICMSTot"}
    
#Aba Sub do Transporte
    tag_transporta = {"CNPJ":"transporta", "xNome":"transporta", "IE":"transporta", "xEnder":"transporta", "xMun":"transporta", "UF":"transporta",
                      "esp":"vol", "pesoL":"vol", "pesoB":"vol"}
    
# Aba Sub do Pagamento
    tag_detPag = {"tPag":"detPag","vPag":"detPag"}

# Aba Sub do Pagamento
    tag_Keyinfo = {"DigestValue":"SignedInfo","X509Certificate":"KeyInfo"}
    tag_X509Data = {"X509Certificate":"X509Data"}

# Aba Sub do Pagamento infProt
    tag_infProt = { "tpAmb":"infProt", "verAplic":"infProt", "chNFe":"infProt",
                    "dhRecbto":"infProt", "nProt":"infProt", "digVal":"infProt", 
                    "cStat":"infProt", "xMotivo":"infProt",}



#=========================== CHAVES
# Identificar valores únicos na coluna "Arquivo"
    chaves_unicas = df_idNFE['Arquivo'].unique()

    # Processar cada chave única
    for chave in chaves_unicas:
        df_idNFE_chave = df_idNFE[df_idNFE['Arquivo'] == chave]
        df_emit_chave = df_emi[df_emi['Arquivo'] == chave]
        df_dest_chave = df_dest[df_dest['Arquivo'] == chave]
        df_det_chave = df_det[df_det['Arquivo'] == chave]
        df_total_chave = df_total[df_total['Arquivo'] == chave]
        df_transp_chave = df_transp[df_transp['Arquivo'] == chave]
        df_paga_chave = df_pagamento[df_pagamento['Arquivo'] == chave]
        df_info_chave = df_info[df_info['Arquivo'] == chave]
        df_assinatura_chave = df_assinatura[df_assinatura['Arquivo'] == chave]
        df_protocolo_chave = df_protocolo[df_protocolo['Arquivo'] == chave]

    # Inicializar o elemento root
        root = ET.Element('nfeProc')
        root.set("xmlns", "http://www.portalfiscal.inf.br/nfe")
        root.set("versao", "4.00")
    # Nova tag NFe
        tagNFe = ET.SubElement(root, 'NFe')
        tagNFe.set("xmlns", "http://www.portalfiscal.inf.br/nfe")
    # Nova tag infNFe
        taginfNfe = ET.SubElement(tagNFe, 'infNFe')
        taginfNfe.set("versao", "4.00")
        taginfNfe.set("id", f"NFe{chave}")
    # Nova tag protNFe


# =============================  DATAFRAME
        ignore_columns = ["Arquivo", "idnNF", "Tipo_ICMS", "Tipo_PIS", "Tipo_COFINS", "NumItem"]
        # Adicionando dados da planilha aba por aba
        dataframe_to_xml (df_idNFE_chave, taginfNfe, 'ide', ignore_columns = ignore_columns)
        dataframe_to_xml (df_emit_chave, taginfNfe, 'emit', sub_element_mapping = sub_emit, ignore_columns = ignore_columns)
        dataframe_to_xml (df_dest_chave, taginfNfe, 'dest', sub_element_mapping = sub_dest, ignore_columns = ignore_columns)
        dataframe_to_xml (df_det_chave, taginfNfe, 'det', sub_element_mapping = tag_impostos, sub_sub_element_mapping = tagICMS,
                          sub_sub_sub_element_mapping = tagICMSTipo, ignore_columns = ignore_columns)  
        dataframe_to_xml (df_total_chave,taginfNfe, 'total', sub_element_mapping = tag_ICMSTot, ignore_columns = ignore_columns)
        dataframe_to_xml (df_transp_chave, taginfNfe, 'transp', sub_element_mapping = tag_transporta, ignore_columns = ignore_columns)
        dataframe_to_xml (df_paga_chave, taginfNfe, 'pag', sub_element_mapping = tag_detPag, ignore_columns=ignore_columns)
        dataframe_to_xml (df_info_chave, taginfNfe, 'infAdic', ignore_columns=ignore_columns)
        dataframe_to_xml (df_assinatura_chave, tagNFe,'Signature', sub_element_mapping = tag_Keyinfo,sub_sub_element_mapping=tag_X509Data, ignore_columns=ignore_columns)
        dataframe_to_xml(df_protocolo_chave, root, 'protNFe', sub_element_mapping=tag_infProt, ignore_columns=ignore_columns)

#Nova tag SignedInfo
# Buscar uma tag ja existente
        tagSignature = root.find('.//Signature')
        tagSignature.set("xmlns", "http://www.w3.org/2000/09/xmldsig#")
        #SigInfo
        tag_SigInfo = root.find('.//SignedInfo')
        #Canonical
        tagCanonical = ET.SubElement(tag_SigInfo, 'CanonicalizationMethod')
        tagCanonical.set("Algorithm", "http://www.w3.org/TR/2001/REC-xml-c14n-20010315")
        #SigMethod
        tagSignatureMethod = ET.SubElement(tag_SigInfo, 'SignatureMethod')
        tagSignatureMethod.set("Algorithm", "http://www.w3.org/2000/09/xmldsig#rsa-sha1")
        #Reference
        tagReference = ET.SubElement(tag_SigInfo, 'Reference')
        tagReference.set("URI",f"#NFe{chave}")
        #Transform
        tagTransforms = ET.SubElement(tagReference,'Transforms')
        tagTransform = ET.SubElement(tagTransforms,'Transform')
        tagTransform.set("Algorithm", "http://www.w3.org/2000/09/xmldsig#enveloped-signature")
        tagTransform = ET.SubElement(tagTransforms,'Transform')
        tagTransform.set("Algorithm", "http://www.w3.org/TR/2001/REC-xml-c14n-20010315")
        #digest methodo
        tagDigestMethod = ET.SubElement(tagReference,'DigestMethod')
        tagDigestMethod.set("Algorithm","http://www.w3.org/2000/09/xmldsig#sha1")
        #excluindo e adicionado o DigestValue
        findDigest = tag_SigInfo.find('.//DigestValue')
        tag_SigInfo.remove(findDigest)  
        tagReference.append(findDigest)
        #protNFe
        findprotNFe = root.find('.//protNFe')
        findprotNFe.set("xmlns",'http://www.portalfiscal.inf.br/nfe')
        findprotNFe.set("versao", "4.00")

        
        for i, finditem in enumerate(root.findall('.//det'), start=1):
            finditem.set("nItem", str(i))


#=========================================================================================================================
        # Converter o elemento root para string XML
        xml_data = ET.tostring(root, encoding='unicode')

        # Caminho para o arquivo XML de saída
        output_xml_file = os.path.join(output_directory, f'NFE_{chave}.xml')
        with open(output_xml_file, 'w', encoding = 'utf-8') as f:
            f.write(xml_data)
        print(f'Arquivo XML para chave {chave} salvo em {output_xml_file}')
