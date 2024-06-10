import pandas as pd
import xml.etree.ElementTree as ET
import glob
import os

# Palavra a ser removida dos nomes das tags
# Função para converter DataFrame para XML e adicionar ao parent_element existente
def df_to_xml(df, parent_element, row_element_name, tag_first_lvl=None, tag_sec_lvl=None, tag_ter_lvl=None, skip_columns=None):
    for _, row in df.iterrows():
        row_element = ET.SubElement(parent_element, row_element_name)    
        for col_name in df.columns:
            # Verifica se o valor é NaN ou espaço Pula a criação da tag se o valor for NaN
            if pd.isna(row[col_name]) or row[col_name] == '' or row[col_name] == ' ':
                continue
            # Pula a criação da tag se a coluna estiver na lista de colunas a serem ignoradas
            if skip_columns and col_name in skip_columns:
                continue 

            if tag_first_lvl and col_name in tag_first_lvl:
                sub_element_name = tag_first_lvl[col_name]
                sub_element = row_element.find(sub_element_name)
                if sub_element is None:
                    sub_element = ET.SubElement(row_element, sub_element_name)
                
                if tag_sec_lvl and col_name in tag_sec_lvl:
                    sub_sub_element_name = tag_sec_lvl[col_name]
                    sub_sub_element = sub_element.find(sub_sub_element_name)
                    if sub_sub_element is None:
                        sub_sub_element = ET.SubElement(sub_element, sub_sub_element_name)
                    
                    if tag_ter_lvl and col_name in tag_ter_lvl:
                        sub_sub_sub_element_name = tag_ter_lvl[col_name]
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
excel_files = glob.glob(r'C:\Users\Igor\Desktop\XML EM UM DICIONARIO\xmlreader\DataFrame_xml/*.xlsx')

# Verificar se há arquivos Excel na pasta especificada
if not excel_files:
    print("Nenhum arquivo Excel encontrado.")
    exit()

# Criar uma pasta para salvar os arquivos XML
output_directory = r'C:\Users\Igor\Desktop\XML EM UM DICIONARIO\xmlreader\DataFrame_xml\XML_Output'
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
    df_compras = pd.read_excel(excel_file, sheet_name="Compras", dtype=str)
    df_respTec = pd.read_excel(excel_file, sheet_name="Resp. Tecnico", dtype=str)
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
    sub_prod = {"NumItem": "prod","cProd":"prod", "cEAN":"prod", "xProd":"prod", "NCM":"prod", "CEST":"prod", "CFOP":"prod",
                "uCom":"prod", "qCom":"prod", "vUnCom":"prod", "vProd":"prod", "cEANTrib":"prod", "uTrib":"prod",
                "qTrib":"prod", "vUnTrib":"prod", "indTot":"prod","xPed":"prod","nFCI":"prod"} 
    # 1 - Impostos
    tag_impostos = {**sub_prod, "Tipo_ICMS":"imposto", "orig":"imposto", "CSOSN":"imposto","ICMS_CST":"imposto","ICMS_modBC": "imposto",
                    "ICMS_vBC": "imposto","ICMS_modBCST": "imposto","ICMS_pRedBC": "imposto","ICMS_pICMS": "imposto",
                     "ICMS_vICMSOp": "imposto","ICMS_pDif": "imposto","ICMS_vICMSDif": "imposto","ICMS_vICMS": "imposto",
                     "ICMS_vICMSDeson": "imposto","ICMS_motDesICMS": "imposto","ICMS_pMVAST": "imposto","ICMS_pRedBCST": "imposto",
                     "ICMS_vBCST": "imposto","ICMS_pICMSST": "imposto","ICMS_vICMSST": "imposto","ICMS_pBCOp": "imposto",
                     "ICMS_UFST": "imposto","ICMS_pFCP": "imposto","ICMS_vFCP": "imposto","ICMS_vBCFCP": "imposto",
                     "ICMS_pFCPST": "imposto","ICMS_vFCPST": "imposto","ICMS_vBCFCPST": "imposto","ICMS_pFCPSTRet": "imposto",
                     "ICMS_vFCPSTRet": "imposto","ICMS_vBCFCPSTRet": "imposto","ICMS_pRedBCEfet": "imposto","ICMS_vBCEfet": "imposto",
                     "ICMS_pICMSEfet": "imposto","ICMS_vICMSEfet": "imposto","ICMS_pST": "imposto","ICMS_qBCMono": "imposto",
                     "ICMS_adRemICMS": "imposto","ICMS_vICMSMono": "imposto","ICMS_qBCMonoReten": "imposto","ICMS_adRemICMSReten": "imposto",
                     "ICMS_vICMSMonoReten": "imposto","ICMS_pRedAdRem": "imposto","ICMS_motRedAdRem": "imposto",
                     "ICMS_motDesICMSST": "imposto","ICMS_pFCPDif": "imposto","ICMS_vFCPDif": "imposto","ICMS_vFCPEfet": "imposto",
                     "ICMS_vICMSMonoOp": "imposto","ICMS_vICMSMonoDif": "imposto","ICMS_qBCMonoDif": "imposto","ICMS_adRemICMSDif": "imposto",
                     "ICMS_vICMSSubstituto": "imposto","ICMS_qBCMonoRet": "imposto","ICMS_adRemICMSRet": "imposto","ICMS_vICMSMonoRet": "imposto",
                    # PIS E COFINS
                    "PIS_CST":"imposto","PIS_vBC":"imposto","PIS_pPIS":"imposto","PIS_vPIS":"imposto","COFINS_CST":"imposto"
                    ,"COFINS_vBC":"imposto","COFINS_pCOFINS":"imposto","COFINS_vCOFINS":"imposto",
                    #IPI
                    "IPI_clEnq":"imposto","IPI_CNPJProd": "imposto","IPI_cSelo": "imposto","IPI_qSelo": "imposto",
                    "IPI_cEnq": "imposto","IPITRIB_CST": "imposto","IPITRIB_vBC": "imposto","IPITRIB_pIPI": "imposto",
                    "IPITRIB_qUnid": "imposto","IPITRIB_vUnid": "imposto","IPITRIB_vIPI": "imposto","IPINT_CST": "imposto"
                    }   
    # 2 - Dentro de ICMS/PISCOFINS/IPI
    tagICMS = { "Tipo_ICMS":"ICMS","orig": "ICMS","CSOSN":"ICMS", "ICMS_CST": "ICMS","ICMS_modBC": "ICMS", "ICMS_vBC": "ICMS","ICMS_modBCST": "ICMS",
               "ICMS_pRedBC": "ICMS", "ICMS_pICMS": "ICMS","ICMS_vICMSOp": "ICMS","ICMS_pDif": "ICMS","ICMS_vICMSDif": "ICMS",
                "ICMS_vICMS": "ICMS","ICMS_vICMSDeson": "ICMS","ICMS_motDesICMS": "ICMS","ICMS_pMVAST": "ICMS",
                "ICMS_pRedBCST": "ICMS","ICMS_vBCST": "ICMS","ICMS_pICMSST": "ICMS","ICMS_vICMSST": "ICMS","ICMS_pBCOp": "ICMS",
                "ICMS_UFST": "ICMS","ICMS_pFCP": "ICMS","ICMS_vFCP": "ICMS","ICMS_vBCFCP": "ICMS","ICMS_pFCPST": "ICMS",
                "ICMS_vFCPST": "ICMS","ICMS_vBCFCPST": "ICMS","ICMS_pFCPSTRet": "ICMS","ICMS_vFCPSTRet": "ICMS",
                "ICMS_vBCFCPSTRet": "ICMS","ICMS_pRedBCEfet": "ICMS","ICMS_vBCEfet": "ICMS","ICMS_pICMSEfet": "ICMS",
                "ICMS_vICMSEfet": "ICMS","ICMS_pST": "ICMS","ICMS_qBCMono": "ICMS","ICMS_adRemICMS": "ICMS",
                "ICMS_vICMSMono": "ICMS","ICMS_qBCMonoReten": "ICMS","ICMS_adRemICMSReten": "ICMS","ICMS_vICMSMonoReten": "ICMS",
                "ICMS_pRedAdRem": "ICMS","ICMS_motRedAdRem": "ICMS","ICMS_motDesICMSST": "ICMS","ICMS_pFCPDif": "ICMS",
                "ICMS_vFCPDif": "ICMS","ICMS_vFCPEfet": "ICMS","ICMS_vICMSMonoOp": "ICMS","ICMS_vICMSMonoDif": "ICMS",
                "ICMS_qBCMonoDif": "ICMS","ICMS_adRemICMSDif": "ICMS","ICMS_vICMSSubstituto": "ICMS","ICMS_qBCMonoRet": "ICMS",
                "ICMS_adRemICMSRet": "ICMS","ICMS_vICMSMonoRet": "ICMS",
                # PIS E COFINS
                "PIS_CST":"PIS","PIS_vBC":"PIS","PIS_pPIS":"PIS","PIS_vPIS":"PIS",
                "COFINS_CST":"COFINS","COFINS_vBC":"COFINS","COFINS_pCOFINS":"COFINS","COFINS_vCOFINS":"COFINS",
                #IPI
                "IPI_clEnq": "IPI","IPI_CNPJProd": "IPI","IPI_cSelo": "IPI","IPI_qSelo": "IPI","IPI_cEnq": "IPI",
                "IPITRIB_CST": "IPI","IPITRIB_vBC": "IPI","IPITRIB_pIPI": "IPI","IPITRIB_qUnid": "IPI","IPITRIB_vUnid": "IPI",
                "IPITRIB_vIPI": "IPI","IPINT_CST": "IPI"
                }
    # 3 - TIPO DE ICMS
    tipodeICMS = "ICMS10"
    tipoPIS = "PISAliq"
    tipoCOFINS = "COFINSAliq"
    tagICMSTipo = {"orig": tipodeICMS,"CSOSN":tipodeICMS, "ICMS_CST": tipodeICMS,"ICMS_modBC": tipodeICMS,"ICMS_vBC": tipodeICMS,"ICMS_modBCST": tipodeICMS,
                   "ICMS_pRedBC": tipodeICMS,"ICMS_pICMS": tipodeICMS,"ICMS_vICMSOp": tipodeICMS,
                    "ICMS_pDif": tipodeICMS,"ICMS_vICMSDif": tipodeICMS,"ICMS_vICMS": tipodeICMS,"ICMS_vICMSDeson": tipodeICMS,
                    "ICMS_motDesICMS": tipodeICMS,"ICMS_pMVAST": tipodeICMS,"ICMS_pRedBCST": tipodeICMS,
                    "ICMS_vBCST": tipodeICMS,"ICMS_pICMSST": tipodeICMS,"ICMS_vICMSST": tipodeICMS,"ICMS_pBCOp": tipodeICMS,
                    "ICMS_UFST": tipodeICMS,"ICMS_pFCP": tipodeICMS,"ICMS_vFCP": tipodeICMS,"ICMS_vBCFCP": tipodeICMS,
                    "ICMS_pFCPST": tipodeICMS,"ICMS_vFCPST": tipodeICMS,"ICMS_vBCFCPST": tipodeICMS,"ICMS_pFCPSTRet": tipodeICMS,
                    "ICMS_vFCPSTRet": tipodeICMS,"ICMS_vBCFCPSTRet": tipodeICMS,"ICMS_pRedBCEfet": tipodeICMS,
                    "ICMS_vBCEfet": tipodeICMS,"ICMS_pICMSEfet": tipodeICMS,"ICMS_vICMSEfet": tipodeICMS,"ICMS_pST": tipodeICMS,
                    "ICMS_qBCMono": tipodeICMS,"ICMS_adRemICMS": tipodeICMS,"ICMS_vICMSMono": tipodeICMS,"ICMS_qBCMonoReten": tipodeICMS,
                    "ICMS_adRemICMSReten": tipodeICMS,"ICMS_vICMSMonoReten": tipodeICMS,"ICMS_pRedAdRem": tipodeICMS,
                    "ICMS_motRedAdRem": tipodeICMS,"ICMS_motDesICMSST": tipodeICMS,"ICMS_pFCPDif": tipodeICMS,"ICMS_vFCPDif": tipodeICMS,
                    "ICMS_vFCPEfet": tipodeICMS,"ICMS_vICMSMonoOp": tipodeICMS,"ICMS_vICMSMonoDif": tipodeICMS,"ICMS_qBCMonoDif": tipodeICMS,
                    "ICMS_adRemICMSDif": tipodeICMS,"ICMS_vICMSSubstituto": tipodeICMS,"ICMS_qBCMonoRet": tipodeICMS,
                    "ICMS_adRemICMSRet": tipodeICMS,"ICMS_vICMSMonoRet": tipodeICMS,
                   # PIS E COFINS
                   "PIS_CST":tipoPIS,"PIS_vBC":tipoPIS,"PIS_pPIS":tipoPIS,"PIS_vPIS":tipoPIS,
                   "COFINS_CST":tipoCOFINS,"COFINS_vBC":tipoCOFINS,"COFINS_pCOFINS":tipoCOFINS,"COFINS_vCOFINS":tipoCOFINS                                       
                    #IPI
                    ,"IPI_clEnq": "IPITrib","IPI_CNPJProd": "IPITrib","IPI_cSelo": "IPITrib","IPI_qSelo": "IPITrib",
                    "IPITRIB_CST": "IPITrib","IPITRIB_vBC": "IPITrib","IPITRIB_pIPI": "IPITrib",
                    "IPITRIB_qUnid": "IPITrib","IPITRIB_vUnid": "IPITrib","IPITRIB_vIPI": "IPITrib","IPINT_CST": "IPINT",
                    }
    # Aba Sub do Total
    tag_ICMSTot = {"vBC": "ICMSTot","vICMS": "ICMSTot","vICMSDeson": "ICMSTot","vFCPUFDest": "ICMSTot", 
                   "vICMSUFDest": "ICMSTot","vICMSUFRemet": "ICMSTot","vFCP": "ICMSTot","vBCST": "ICMSTot",
                   "vST": "ICMSTot","vFCPST": "ICMSTot","vFCPSTRet": "ICMSTot","vProd": "ICMSTot","vFrete": "ICMSTot",
                   "vSeg": "ICMSTot","vDesc": "ICMSTot","vII": "ICMSTot","vIPI": "ICMSTot","vIPIDevol": "ICMSTot",
                   "vPIS": "ICMSTot","vCOFINS": "ICMSTot","vOutro": "ICMSTot","vNF": "ICMSTot","vTotTrib": "ICMSTot"}
    #Aba Sub do Transporte
    tag_transporta = {"CNPJ":"transporta", "xNome":"transporta", "IE":"transporta", "xEnder":"transporta", "xMun":"transporta", "UF":"transporta"}
    # Aba Sub do Pagamento
    tag_detPag = {"indPag":"detPag", "tPag":"detPag","xPag":"detPag","vPag":"detPag","vPag":"detPag","vTroco":"detPag",
                  "CARD_tpIntegra":"CARD", "CARD_CNPJ":"CARD", "CARD_tBand":"CARD", "CARD_cAut":"CARD"}
    # Aba Sub do 
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
        df_cobranca_chave = df_cobranca[df_cobranca['Arquivo'] == chave]
        df_paga_chave = df_pagamento[df_pagamento['Arquivo'] == chave]
        df_info_chave = df_info[df_info['Arquivo'] == chave]
        df_compras_chave = df_compras[df_compras['Arquivo'] == chave]
        df_respTec_chave = df_respTec[df_respTec['Arquivo'] == chave]
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
        taginfNfe.set("Id", f"NFe{chave}")
        


# =============================  DATAFRAME
        skip_columns = ["Arquivo", "idnNF", "NumItem"]   
        # Adicionando dados da planilha aba por aba
        df_to_xml (df_idNFE_chave, taginfNfe, 'ide', skip_columns=skip_columns)
        df_to_xml (df_emit_chave, taginfNfe, 'emit', tag_first_lvl = sub_emit, skip_columns=skip_columns)
        df_to_xml (df_dest_chave, taginfNfe, 'dest', tag_first_lvl = sub_dest, skip_columns=skip_columns)
        df_to_xml (df_det_chave, taginfNfe, 'det', tag_first_lvl = tag_impostos, tag_sec_lvl=tagICMS, tag_ter_lvl = tagICMSTipo, skip_columns=skip_columns)
        df_to_xml (df_total_chave,taginfNfe, 'total', tag_first_lvl = tag_ICMSTot, skip_columns=skip_columns)    
        df_to_xml (df_assinatura_chave, tagNFe,'Signature', tag_first_lvl = tag_Keyinfo, tag_sec_lvl = tag_X509Data, skip_columns=skip_columns)
        df_to_xml (df_protocolo_chave, root, 'protNFe', tag_first_lvl = tag_infProt, skip_columns=skip_columns)
        
        # Nova tag transporte        
        tagTrans = ET.SubElement(taginfNfe, 'transp')
        transport = ET.SubElement(tagTrans, 'transporta')
        df_to_xml (df_transp_chave, tagTrans, 'vol',skip_columns=skip_columns)
        # Encontrando e movendo elementos de transporte
        elements = ['CNPJ', 'xNome', 'IE', 'xEnder', 'xMun', 'UF']
        transpfind = tagTrans.find('.//vol')
        for elem in elements:
            found_elem = transpfind.find(f'.//{elem}')
            transpfind.remove(found_elem)
            transport.append(found_elem)
        # TAG modFrete
        modfrete = transpfind.find('.//modFrete')
        transpfind.remove(modfrete)
        tagTrans.insert(0, modfrete)
        #   CRIACAO DE TAG COBR TAG  FAT
        tagCobr = ET.SubElement(taginfNfe, 'cobr')
        tagfaturamento = ET.SubElement(tagCobr, 'fat')

        
        df_to_xml (df_cobranca_chave, tagCobr, 'dup', skip_columns = skip_columns)
        df_to_xml (df_paga_chave, taginfNfe, 'pag', tag_first_lvl = tag_detPag, skip_columns=skip_columns)
        df_to_xml (df_info_chave, taginfNfe, 'infAdic', skip_columns=skip_columns)
        df_to_xml (df_compras_chave, taginfNfe, 'compra', skip_columns=skip_columns)
        df_to_xml (df_respTec_chave, taginfNfe, 'infRespTec', skip_columns=skip_columns)
    
    # Movimentacao de TAGS
        # Nova tag SignedInfo
        tagSignature = root.find('.//Signature')
        tagSignature.set("xmlns", "http://www.w3.org/2000/09/xmldsig#")
        #SigInfo
        tag_SigInfo = root.find('.//SignedInfo')
        tag_SigInfo.set("xmlns", "http://www.w3.org/2000/09/xmldsig#")
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
        # # Adicionarndo TAG cBenef
        # for taginfNfe in root.findall('.//det'):
        #     findtagBenef = taginfNfe.find('.//prod')
        #     tagBenef = ET.SubElement(findtagBenef, 'cBenef')

        # movendo TAG FAT
        fatFind = ['FAT_nFat', 'FAT_vDesc', 'FAT_vOrig', 'FAT_vLiq']
        for fat in root.findall('.//dup'):
            for tag in fatFind:
                FAT_nFat = fat.find(tag)
                if FAT_nFat is not None:
                    fat.remove(FAT_nFat)
                    tagfaturamento.append(FAT_nFat) # excluir         
        for i, finditem in enumerate(root.findall('.//det'), start=1):
            finditem.set("nItem", str(i))

        # Percorrer cada elemento <det> do XML e alterar a tag TIPOICMS
        for det_element in root.findall('.//det'):
            tipo_icms = det_element.find('.//Tipo_ICMS').text
            icms10 = det_element.find('.//ICMS/ICMS10')
            if icms10 is not None:
                icms10.tag = tipo_icms
        # Percorrer cada elemento <det> do XML e excluir a tag TIPOICMS
        for detelement in root.findall('.//det'):
            icmselement = detelement.find('.//ICMS')
            tipo_icms_element = icmselement.find('.//Tipo_ICMS')
            icmselement.remove(tipo_icms_element)


    #================================================================================ pis e cofins
        # Percorrer cada elemento <det> do XML e alterar a tag TIPOICMS
        for det_element in root.findall('.//det'):
            tipo_pis = det_element.find('.//Tipo_PIS').text
            pisaliq = det_element.find('.//PISAliq')
            cofinsaliq = det_element.find('.//COFINSAliq')
            if pisaliq is not None:
                pisaliq.tag = (f'PIS{tipo_pis}')
            if cofinsaliq is not None:
                cofinsaliq.tag = (f'COFINS{tipo_pis}')

            piselement = det_element.find('Tipo_PIS')
            det_element.remove(piselement)
            cofinslement = det_element.find('Tipo_COFINS')
            det_element.remove(cofinslement)

    #========================================== TIRANDO NOME DAS TAG tipo_de_icms ===============================================================================
        def remove_words_from_tag_names(element):
            if '_' in element.tag:
                element.tag = element.tag.split('_', 1)[1]
            # Fazer o mesmo para todos os filhos do elemento
            for child in list(element):
                remove_words_from_tag_names(child)
        # Remover as palavras dos nomes das tags de todo o XML
        remove_words_from_tag_names(root)

#=========================================================================================================================
        # Converter o elemento root para string XML
        xml_data = ET.tostring(root, encoding='unicode')

        # Caminho para o arquivo XML de saída
        output_xml_file = os.path.join(output_directory, f'NFE_{chave}.xml')
        with open(output_xml_file, 'w', encoding = 'utf-8') as f:
            f.write(xml_data)
        print(f'Arquivo XML para chave {chave} salvo em {output_xml_file}')
