def exceltoXml ():    
    # df_to_xml`, converte um DataFrame do pandas em elementos XML, organizando-os hierarquicamente conforme as especificações fornecidas por tags de primeiro, segundo e terceiro níveis e evitando colunas especificadas para pular.
    import pandas as pd
    import xml.etree.ElementTree as ET
    import glob
    import os
    from funcoes.leitura_excel import df_to_xml
    from funcoes.redenifir_tags import remover_
    from funcoes.selecionar import select_folder, select_excel_file

    # Função principal para processamento de arquivos Excel e geração de XML
    path_excel = select_excel_file("Selecione o arquivo Excel")
    excel_files = glob.glob(path_excel)

    if not excel_files:
        print("Nenhum arquivo Excel encontrado.")
        exit()

    path_salve = select_folder("Selecione onde salvar os arquivos XML")
    output_directory = (path_salve) 
    os.makedirs(output_directory, exist_ok=True)


    # Mapas para elementos XML
    sub_emit = {"xLgr": "enderEmit", "nro": "enderEmit", "xCpl": "enderEmit", "xBairro": "enderEmit", "cMun": "enderEmit",
                "xMun": "enderEmit", "UF": "enderEmit", "CEP": "enderEmit", "cPais": "enderEmit", "xPais": "enderEmit", 
                "fone": "enderEmit"}

    sub_dest = {"xLgr": "enderDest", "nro": "enderDest", "xCpl": "enderDest", "xBairro": "enderDest", "cMun": "enderDest",
                "xMun": "enderDest", "UF": "enderDest", "CEP": "enderDest", "cPais": "enderDest", "xPais": "enderDest", 
                "fone": "enderDest"}

    sub_prod = {"NumItem": "prod","cProd": "prod", "cEAN": "prod", "xProd": "prod", "NCM": "prod", "CEST": "prod", 
                "CFOP": "prod", "uCom": "prod", "qCom": "prod", "vUnCom": "prod", "vProd": "prod", "cEANTrib": "prod", 
                "uTrib": "prod", "qTrib": "prod", "vUnTrib": "prod", "indTot": "prod","xPed": "prod", "nFCI": "prod","nItemPed":"prod"}

    tag_impostos = {**sub_prod, "vTotTrib":"imposto", "Tipo_ICMS": "imposto", "orig": "imposto", "CSOSN": "imposto","ICMS_CST": "imposto",
                    "ICMS_modBC": "imposto", "ICMS_vBC": "imposto","ICMS_modBCST": "imposto","ICMS_pRedBC": "imposto",
                    "ICMS_pICMS": "imposto", "ICMS_vICMSOp": "imposto","ICMS_pDif": "imposto","ICMS_vICMSDif": "imposto",
                    "ICMS_vICMS": "imposto","ICMS_vICMSDeson": "imposto","ICMS_motDesICMS": "imposto","ICMS_pMVAST": "imposto",
                    "ICMS_pRedBCST": "imposto","ICMS_vBCST": "imposto","ICMS_pICMSST": "imposto","ICMS_vICMSST": "imposto",
                    "ICMS_pBCOp": "imposto","ICMS_UFST": "imposto","ICMS_pFCP": "imposto","ICMS_vFCP": "imposto",
                    "ICMS_vBCFCP": "imposto","ICMS_pFCPST": "imposto","ICMS_vFCPST": "imposto","ICMS_vBCFCPST": "imposto",
                    "ICMS_pFCPSTRet": "imposto","ICMS_vFCPSTRet": "imposto","ICMS_vBCFCPSTRet": "imposto","ICMS_pRedBCEfet": "imposto",
                    "ICMS_vBCEfet": "imposto","ICMS_pICMSEfet": "imposto","ICMS_vICMSEfet": "imposto","ICMS_pST": "imposto",
                    "ICMS_qBCMono": "imposto","ICMS_adRemICMS": "imposto","ICMS_vICMSMono": "imposto","ICMS_qBCMonoReten": "imposto",
                    "ICMS_adRemICMSReten": "imposto","ICMS_vICMSMonoReten": "imposto","ICMS_pRedAdRem": "imposto","ICMS_motRedAdRem": "imposto",
                    "ICMS_motDesICMSST": "imposto","ICMS_pFCPDif": "imposto","ICMS_vFCPDif": "imposto","ICMS_vFCPEfet": "imposto",
                    "ICMS_vICMSMonoOp": "imposto","ICMS_vICMSMonoDif": "imposto","ICMS_qBCMonoDif": "imposto","ICMS_adRemICMSDif": "imposto",
                    "ICMS_vICMSSubstituto": "imposto","ICMS_qBCMonoRet": "imposto","ICMS_adRemICMSRet": "imposto","ICMS_vICMSMonoRet": "imposto",
                    "PIS_CST":"imposto","PIS_vBC":"imposto","PIS_pPIS":"imposto","PIS_vPIS":"imposto","COFINS_CST":"imposto",
                    "COFINS_vBC":"imposto","COFINS_pCOFINS":"imposto","COFINS_vCOFINS":"imposto","IPI_clEnq":"imposto",
                    "IPI_CNPJProd": "imposto","IPI_cSelo": "imposto","IPI_qSelo": "imposto","IPI_cEnq": "imposto",
                    "IPITRIB_CST": "imposto","IPITRIB_vBC": "imposto","IPITRIB_pIPI": "imposto","IPITRIB_qUnid": "imposto",
                    "IPITRIB_vUnid": "imposto","IPITRIB_vIPI": "imposto","IPINT_CST": "imposto"}

    tagICMS = {"Tipo_ICMS":"ICMS","orig": "ICMS","CSOSN":"ICMS", "ICMS_CST": "ICMS","ICMS_modBC": "ICMS", "ICMS_vBC": "ICMS",
                "ICMS_modBCST": "ICMS", "ICMS_pRedBC": "ICMS", "ICMS_pICMS": "ICMS","ICMS_vICMSOp": "ICMS","ICMS_pDif": "ICMS",
                "ICMS_vICMSDif": "ICMS","ICMS_vICMS": "ICMS","ICMS_vICMSDeson": "ICMS","ICMS_motDesICMS": "ICMS","ICMS_pMVAST": "ICMS",
                "ICMS_pRedBCST": "ICMS","ICMS_vBCST": "ICMS","ICMS_pICMSST": "ICMS","ICMS_vICMSST": "ICMS","ICMS_pBCOp": "ICMS",
                "ICMS_UFST": "ICMS","ICMS_pFCP": "ICMS","ICMS_vFCP": "ICMS","ICMS_vBCFCP": "ICMS","ICMS_pFCPST": "ICMS",
                "ICMS_vFCPST": "ICMS","ICMS_vBCFCPST": "ICMS","ICMS_pFCPSTRet": "ICMS","ICMS_vFCPSTRet": "ICMS",
                "ICMS_vBCFCPSTRet": "ICMS","ICMS_pRedBCEfet": "ICMS","ICMS_vBCEfet": "ICMS","ICMS_pICMSEfet": "ICMS",
                "ICMS_vICMSEfet": "ICMS","ICMS_pST": "ICMS","ICMS_qBCMono": "ICMS","ICMS_adRemICMS": "ICMS",
                "ICMS_vICMSMono": "ICMS","ICMS_qBCMonoReten": "ICMS","ICMS_adRemICMSReten": "ICMS","ICMS_vICMSMonoReten": "ICMS",
                "ICMS_pRedAdRem": "ICMS","ICMS_motRedAdRem": "ICMS","ICMS_motDesICMSST": "ICMS","ICMS_pFCPDif": "ICMS",
                "ICMS_vFCPDif": "ICMS","ICMS_vFCPEfet": "ICMS","ICMS_vICMSMonoOp": "ICMS","ICMS_vICMSMonoDif": "ICMS",
                "ICMS_qBCMonoDif": "ICMS","ICMS_adRemICMSDif": "ICMS","ICMS_vICMSSubstituto": "ICMS","ICMS_qBCMonoRet": "ICMS",
                "ICMS_adRemICMSRet": "ICMS","ICMS_vICMSMonoRet": "ICMS", "PIS_CST": "PIS","PIS_vBC": "PIS","PIS_pPIS": "PIS",
                "PIS_vPIS": "PIS","COFINS_CST": "COFINS","COFINS_vBC": "COFINS","COFINS_pCOFINS": "COFINS","COFINS_vCOFINS": "COFINS",
                "IPI_clEnq": "IPI","IPI_CNPJProd": "IPI","IPI_cSelo": "IPI","IPI_qSelo": "IPI","IPI_cEnq": "IPI",
                "IPITRIB_CST": "IPI","IPITRIB_vBC": "IPI","IPITRIB_pIPI": "IPI","IPITRIB_qUnid": "IPI","IPITRIB_vUnid": "IPI",
                "IPITRIB_vIPI": "IPI","IPINT_CST": "IPI"}

    tipodeICMS = "ICMS10"
    tipoPIS = "PISAliq"
    tipoCOFINS = "COFINSAliq"

    tagICMSTipo = {"orig": tipodeICMS,"CSOSN":tipodeICMS, "ICMS_CST": tipodeICMS,"ICMS_modBC": tipodeICMS,"ICMS_vBC": tipodeICMS,
                    "ICMS_modBCST": tipodeICMS,"ICMS_pRedBC": tipodeICMS,"ICMS_pICMS": tipodeICMS,"ICMS_vICMSOp": tipodeICMS,
                    "ICMS_pDif": tipodeICMS,"ICMS_vICMSDif": tipodeICMS,"ICMS_vICMS": tipodeICMS,"ICMS_vICMSDeson": tipodeICMS,
                    "ICMS_motDesICMS": tipodeICMS,"ICMS_pMVAST": tipodeICMS,"ICMS_pRedBCST": tipodeICMS,"ICMS_vBCST": tipodeICMS,
                    "ICMS_pICMSST": tipodeICMS,"ICMS_vICMSST": tipodeICMS,"ICMS_pBCOp": tipodeICMS,"ICMS_UFST": tipodeICMS,
                    "ICMS_pFCP": tipodeICMS,"ICMS_vFCP": tipodeICMS,"ICMS_vBCFCP": tipodeICMS,"ICMS_pFCPST": tipodeICMS,
                    "ICMS_vFCPST": tipodeICMS,"ICMS_vBCFCPST": tipodeICMS,"ICMS_pFCPSTRet": tipodeICMS,"ICMS_vFCPSTRet": tipodeICMS,
                    "ICMS_vBCFCPSTRet": tipodeICMS,"ICMS_pRedBCEfet": tipodeICMS,"ICMS_vBCEfet": tipodeICMS,"ICMS_pICMSEfet": tipodeICMS,
                    "ICMS_vICMSEfet": tipodeICMS,"ICMS_pST": tipodeICMS,"ICMS_qBCMono": tipodeICMS,"ICMS_adRemICMS": tipodeICMS,
                    "ICMS_vICMSMono": tipodeICMS,"ICMS_qBCMonoReten": tipodeICMS,"ICMS_adRemICMSReten": tipodeICMS,
                    "ICMS_vICMSMonoReten": tipodeICMS,"ICMS_pRedAdRem": tipodeICMS,"ICMS_motRedAdRem": tipodeICMS,
                    "ICMS_motDesICMSST": tipodeICMS,"ICMS_pFCPDif": tipodeICMS,"ICMS_vFCPDif": tipodeICMS,"ICMS_vFCPEfet": tipodeICMS,
                    "ICMS_vICMSMonoOp": tipodeICMS,"ICMS_vICMSMonoDif": tipodeICMS,"ICMS_qBCMonoDif": tipodeICMS,
                    "ICMS_adRemICMSDif": tipodeICMS,"ICMS_vICMSSubstituto": tipodeICMS,"ICMS_qBCMonoRet": tipodeICMS,
                    "ICMS_adRemICMSRet": tipodeICMS,"ICMS_vICMSMonoRet": tipodeICMS, "PIS_CST":tipoPIS,"PIS_vBC":tipoPIS,
                    "PIS_pPIS":tipoPIS,"PIS_vPIS":tipoPIS,"COFINS_CST":tipoCOFINS,"COFINS_vBC":tipoCOFINS,
                    "COFINS_pCOFINS":tipoCOFINS,"COFINS_vCOFINS":tipoCOFINS, "IPI_clEnq": "IPITrib","IPI_CNPJProd": "IPITrib",
                    "IPI_cSelo": "IPITrib","IPI_qSelo": "IPITrib", "IPITRIB_CST": "IPITrib","IPITRIB_vBC": "IPITrib",
                    "IPITRIB_pIPI": "IPITrib", "IPITRIB_qUnid": "IPITrib","IPITRIB_vUnid": "IPITrib","IPITRIB_vIPI": "IPITrib",
                    "IPINT_CST": "IPINT"}

    tag_ICMSTot = {"vBC": "ICMSTot","vICMS": "ICMSTot","vICMSDeson": "ICMSTot","vFCPUFDest": "ICMSTot", "vICMSUFDest": "ICMSTot",
                    "vICMSUFRemet": "ICMSTot","vFCP": "ICMSTot","vBCST": "ICMSTot","vST": "ICMSTot","vFCPST": "ICMSTot",
                    "vFCPSTRet": "ICMSTot","vProd": "ICMSTot","vFrete": "ICMSTot","vSeg": "ICMSTot","vDesc": "ICMSTot",
                    "vII": "ICMSTot","vIPI": "ICMSTot","vIPIDevol": "ICMSTot","vPIS": "ICMSTot","vCOFINS": "ICMSTot",
                    "vOutro": "ICMSTot","vNF": "ICMSTot","vTotTrib": "ICMSTot"}

    tag_transporta = {"CNPJ":"transporta", "xNome":"transporta", "IE":"transporta", "xEnder":"transporta", "xMun":"transporta", "UF":"transporta"}

    tag_detPag = {"indPag": "detPag", "tPag": "detPag", "xPag": "detPag", "vPag": "detPag", "vTroco": "detPag",
                    "CARD_tpIntegra": "CARD", "CARD_CNPJ": "CARD", "CARD_tBand": "CARD", "CARD_cAut": "CARD"}

    tag_Keyinfo = {"DigestValue": "SignedInfo", "X509Certificate": "KeyInfo"}
    tag_X509Data = {"X509Certificate": "X509Data"}

    tag_infProt = {"tpAmb": "infProt", "verAplic": "infProt", "chNFe": "infProt", "dhRecbto": "infProt",
                    "nProt": "infProt", "digVal": "infProt", "cStat": "infProt", "xMotivo": "infProt"}
    for excel_file in excel_files:    
        df_idNFE = pd.read_excel(excel_file, sheet_name="Identificação NFE", dtype=str)
        df_emi = pd.read_excel(excel_file, sheet_name="Emitente", dtype=str)
        df_avulsa = pd.read_excel(excel_file, sheet_name="Avulsa", dtype=str)
        df_dest = pd.read_excel(excel_file, sheet_name="Destinatário", dtype=str)
        df_retirada = pd.read_excel(excel_file, sheet_name="Retirada",dtype=str)
        df_entrega = pd.read_excel(excel_file, sheet_name="Entrega",dtype=str)
        df_autorizada = pd.read_excel(excel_file, sheet_name="Autorizadas",dtype=str)                            
        df_det = pd.read_excel(excel_file, sheet_name="Itens", dtype=str)
        df_total = pd.read_excel(excel_file, sheet_name="Total", dtype=str)
        df_transp = pd.read_excel(excel_file, sheet_name="Transportadora", dtype=str)
        df_cobranca = pd.read_excel(excel_file, sheet_name="Cobrança", dtype=str)
        df_pagamento = pd.read_excel(excel_file, sheet_name="Pagamento", dtype=str)
        df_intermed = pd.read_excel(excel_file, sheet_name="Intermediador", dtype=str)
        df_info = pd.read_excel(excel_file, sheet_name="Inf. Adicional", dtype=str)
        df_exportacao = pd.read_excel(excel_file, sheet_name="Exportação",dtype=str)
        df_compras = pd.read_excel(excel_file, sheet_name="Compras", dtype=str)
        df_respTec = pd.read_excel(excel_file, sheet_name="Resp. Tecnico", dtype=str)
        df_assinatura = pd.read_excel(excel_file, sheet_name="Assinatura", dtype=str)
        df_protocolo = pd.read_excel(excel_file, sheet_name="Protocolo", dtype=str)
        
        chaves_unicas = df_idNFE['Arquivo'].unique()

        for chave in chaves_unicas:
            df_idNFE_chave = df_idNFE[df_idNFE['Arquivo'] == chave]
            df_emit_chave = df_emi[df_emi['Arquivo'] == chave]
            df_avulsa_chave = df_avulsa[df_avulsa['Arquivo'] == chave]
            df_dest_chave = df_dest[df_dest['Arquivo'] == chave]
            df_retirada_chave = df_retirada[df_retirada['Arquivo'] == chave]
            df_entrega_chave = df_entrega[df_entrega['Arquivo'] == chave]
            df_autoriza_chave = df_autorizada[df_autorizada['Arquivo'] == chave]
            df_det_chave = df_det[df_det['Arquivo'] == chave]
            df_total_chave = df_total[df_total['Arquivo'] == chave]
            df_transp_chave = df_transp[df_transp['Arquivo'] == chave]
            df_cobranca_chave = df_cobranca[df_cobranca['Arquivo'] == chave]
            df_paga_chave = df_pagamento[df_pagamento['Arquivo'] == chave]
            df_intermed_chave = df_intermed[df_intermed['Arquivo'] == chave]
            df_info_chave = df_info[df_info['Arquivo'] == chave]
            df_exportacao_chave = df_exportacao[df_exportacao['Arquivo'] == chave]
            df_compras_chave = df_compras[df_compras['Arquivo'] == chave]
            df_respTec_chave = df_respTec[df_respTec['Arquivo'] == chave]
            df_assinatura_chave = df_assinatura[df_assinatura['Arquivo'] == chave]
            df_protocolo_chave = df_protocolo[df_protocolo['Arquivo'] == chave]

            # criação de TAGS
            root = ET.Element('nfeProc')
            root.set("xmlns", "http://www.portalfiscal.inf.br/nfe")
            root.set("versao", "4.00")
            tagNFe = ET.SubElement(root, 'NFe')
            tagNFe.set("xmlns", "http://www.portalfiscal.inf.br/nfe")
            taginfNfe = ET.SubElement(tagNFe, 'infNFe')
            taginfNfe.set("versao", "4.00")
            taginfNfe.set("Id", f"NFe{chave}")

            

            # pular algumas colunas
            skip_columns = ["Arquivo", "idnNF", "NumItem","versao_XML"]

            # Chamadas para df_to_xml para as outras planilhas
            df_to_xml(df_idNFE_chave, taginfNfe, 'ide', skip_columns=skip_columns)
            df_to_xml(df_emit_chave, taginfNfe, 'emit', tag_first_lvl=sub_emit, skip_columns=skip_columns)
            df_to_xml(df_avulsa_chave,taginfNfe, 'avulsa', skip_columns=skip_columns)
            df_to_xml(df_dest_chave, taginfNfe, 'dest', tag_first_lvl=sub_dest, skip_columns=skip_columns)
            df_to_xml(df_retirada_chave, taginfNfe, 'retirada', skip_columns=skip_columns)
            df_to_xml(df_entrega_chave, taginfNfe, 'entrega', skip_columns=skip_columns)
            df_to_xml(df_autoriza_chave, taginfNfe, 'autXML', skip_columns=skip_columns)
            df_to_xml(df_det_chave, taginfNfe, 'det', tag_first_lvl=tag_impostos, tag_sec_lvl=tagICMS, tag_ter_lvl=tagICMSTipo, skip_columns=skip_columns)
            df_to_xml(df_total_chave, taginfNfe, 'total', tag_first_lvl=tag_ICMSTot, skip_columns=skip_columns)
            df_to_xml(df_assinatura_chave, tagNFe, 'Signature', tag_first_lvl=tag_Keyinfo, tag_sec_lvl=tag_X509Data, skip_columns=skip_columns)
            df_to_xml(df_protocolo_chave, root, 'protNFe', tag_first_lvl=tag_infProt, skip_columns=skip_columns)

            # Transporte
            tagTrans = ET.SubElement(taginfNfe, 'transp')
            transport = ET.SubElement(tagTrans, 'transporta')
            #try:
            #trasportCnpj = transport.find('//CNPJ')
            df_to_xml(df_transp_chave, tagTrans, 'vol', skip_columns=skip_columns)
            elements = ['CNPJ', 'xNome', 'IE', 'xEnder', 'xMun', 'UF']
            transpfind = tagTrans.find('.//vol')
            if  transpfind is not None:
                for elem in elements:
                    found_elem = transpfind.find(f'.//{elem}')
                    if found_elem is not None:
                        transpfind.remove(found_elem)
                        transport.append(found_elem)
                modfrete = transpfind.find('.//modFrete')
                if modfrete is not None:
                    transpfind.remove(modfrete)
                    tagTrans.insert(0, modfrete)
            #except Exception as e:
            #    tagTrans.remove(transport)

            # Cobrança
            tagCobr = ET.SubElement(taginfNfe, 'cobr')
            tagfaturamento = ET.SubElement(tagCobr, 'fat')
            #try:
            tagfatura = tagCobr.find ('.//nFat')
            df_to_xml(df_cobranca_chave, tagCobr, 'dup', skip_columns=skip_columns)
            fatFind = ['FAT_nFat', 'FAT_vDesc', 'FAT_vOrig', 'FAT_vLiq']
            for fat in root.findall('.//dup'):
                for tag in fatFind:
                    cobranca_FAT_nFat = fat.find(tag)
                    if cobranca_FAT_nFat is not None:
                        fat.remove(cobranca_FAT_nFat)
                        tagfaturamento.append(cobranca_FAT_nFat)
            #except Exception as e:
            #    print('excluir CobranÇa')# ----------------------------------------------------

            df_to_xml(df_paga_chave, taginfNfe, 'pag', tag_first_lvl=tag_detPag, skip_columns=skip_columns)
            df_to_xml(df_intermed_chave,taginfNfe,'idCadIntTran', skip_columns=skip_columns)
            df_to_xml(df_info_chave, taginfNfe, 'infAdic', skip_columns=skip_columns)
            df_to_xml(df_exportacao_chave,taginfNfe, 'exporta', skip_columns=skip_columns)
            df_to_xml(df_compras_chave, taginfNfe, 'compra', skip_columns=skip_columns)
            df_to_xml(df_respTec_chave, taginfNfe, 'infRespTec', skip_columns=skip_columns)
            # Ajuster nas TAGS
            # Assinatura
            tagSignature = root.find('.//Signature')
            if tagSignature is not None:
                tagSignature.set("xmlns", "http://www.w3.org/2000/09/xmldsig#")
            tag_SigInfo = root.find('.//SignedInfo')
            if  tag_SigInfo is not None:
                tagCanonical = ET.SubElement(tag_SigInfo, 'CanonicalizationMethod')
                tagCanonical.set("Algorithm", "http://www.w3.org/TR/2001/REC-xml-c14n-20010315")
                tagSignatureMethod = ET.SubElement(tag_SigInfo, 'SignatureMethod')
                tagSignatureMethod.set("Algorithm", "http://www.w3.org/2000/09/xmldsig#rsa-sha1")
                tagReference = ET.SubElement(tag_SigInfo, 'Reference')
                tagReference.set("URI", f"#NFe{chave}")
                tagTransforms = ET.SubElement(tagReference, 'Transforms')
                tagTransform = ET.SubElement(tagTransforms, 'Transform')
                tagTransform.set("Algorithm", "http://www.w3.org/2000/09/xmldsig#enveloped-signature")
                tagTransform = ET.SubElement(tagTransforms, 'Transform')
                tagTransform.set("Algorithm", "http://www.w3.org/TR/2001/REC-xml-c14n-20010315")
                tagDigestMethod = ET.SubElement(tagReference, 'DigestMethod')
                tagDigestMethod.set("Algorithm", "http://www.w3.org/2000/09/xmldsig#sha1")
                findDigest = tag_SigInfo.find('.//DigestValue')
                if  findDigest is not None:
                    tag_SigInfo.remove(findDigest)
                    tagReference.append(findDigest)
                # protNFe
                findprotNFe = root.find('.//protNFe')
                if findprotNFe is not None:
                    findprotNFe.set("xmlns", 'http://www.portalfiscal.inf.br/nfe')
                    findprotNFe.set("versao", '4.00')
            


            for i, finditem in enumerate(root.findall('.//det'), start=1):
                finditem.set("nItem", str(i))
                
            for det_element in root.findall('.//det'):
                tipo_icms_element = det_element.find('.//Tipo_ICMS')
                if tipo_icms_element is not None and tipo_icms_element.text is not None:
                    tipo_icms = tipo_icms_element.text
                    icms10 = det_element.find('.//ICMS/ICMS10')
                    if icms10 is not None:
                        icms10.tag = tipo_icms

            for detelement in root.findall('.//det'):
                icmselement = detelement.find('.//ICMS')
                if icmselement is not None:
                    tipo_icms_element = icmselement.find('.//Tipo_ICMS')
                    if tipo_icms_element is not None:
                        icmselement.remove(tipo_icms_element)

            for det_element in root.findall('.//det'):
                tipo_pis = det_element.find('.//Tipo_PIS')
                if tipo_pis is not None:
                    tipo_pis = tipo_pis.text
                pisaliq = det_element.find('.//PISAliq')
                cofinsaliq = det_element.find('.//COFINSAliq')
                if pisaliq is not None:
                    pisaliq.tag = f'PIS{tipo_pis}'
                if cofinsaliq is not None:
                    cofinsaliq.tag = f'COFINS{tipo_pis}'

                pis_element = det_element.find('Tipo_PIS')
                if  pis_element is not None:
                    det_element.remove(pis_element)
                cofins_element = det_element.find('Tipo_COFINS')
                if  cofins_element is not None:            
                    det_element.remove(cofins_element)

            remover_(root)

            xml_data = ET.tostring(root, encoding='unicode')

            output_xml_file = os.path.join(output_directory, f'NFE_{chave}.xml')
            with open(output_xml_file, 'w', encoding='utf-8') as f:
                f.write(xml_data)
            print(f'Arquivo XML para chave {chave} salvo em {output_xml_file}')
