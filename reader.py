import os
import xml.etree.ElementTree as Et
import pandas as pd

class ReadXML:
    def __init__(self, directory) -> None:
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"The directory {directory} does not exist.")
        self.directory = directory

    def all_files(self):
        return [os.path.join(self.directory, arq) for arq in os.listdir(self.directory)
                if arq.lower().endswith(".xml")]

    def nfe_data(self, xml_file):
        tree = Et.parse(xml_file)
        root = tree.getroot()
        nsNfe = {"ns": "http://www.portalfiscal.inf.br/nfe"}
        infNFe = root.find('ns:NFe/ns:infNFe', nsNfe)
        dados = {
            "Identificação NFE": [],
            "Emitente": [],
            "Destinatário":[],
            "Itens":[],
            "Total":[],
            "Transportadora":[],
            "Pagamento":[],
            "Inf. Adicional":[],
            "Assinatura":[],
            "Protocolo":[]
        }

        # Lista para armazenar os dados das notas fiscais
        notas = []
        chave = self.check_none(root.find("./ns:protNFe/ns:infProt/ns:chNFe", nsNfe))
        nNF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:nNF", nsNfe))


#======================================================================== Identificação NFE ============================================================
        versao_XML = root.find('ns:NFe/ns:infNFe', nsNfe).get('versao')
        arquivo = self.check_none(root.find("./ns:protNFe/ns:infProt/ns:chNFe", nsNfe))
        cUF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:cUF", nsNfe))
        cNF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:cNF", nsNfe))
        natOp = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:natOp", nsNfe))
        indPag = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:indPag", nsNfe))
        mod = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:mod", nsNfe))
        serie = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:serie", nsNfe))
        nNF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:nNF", nsNfe))
        dhEmi = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:dhEmi", nsNfe))
        dhSaiEnt = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:dhSaiEnt", nsNfe))
        hSaiEnt = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:hSaiEnt", nsNfe))
        tpNF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:tpNF", nsNfe))
        idDest = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:idDest", nsNfe))
        cMunFG = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:cMunFG", nsNfe))
        tpImp = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:tpImp", nsNfe))
        tpEmis = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:tpEmis", nsNfe))
        cDV = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:cDV", nsNfe))
        tpAmb = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:tpAmb", nsNfe))
        finNFe = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:finNFe", nsNfe))
        indFinal = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:indFinal", nsNfe))
        indPres = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:indPres", nsNfe))
        indIntermed = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:indIntermed", nsNfe))
        procEmi = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:procEmi", nsNfe))
        verProc = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:verProc", nsNfe))
        dhCont = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:dhCont", nsNfe))
        xJust = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:xJust", nsNfe))
        nFREF_refNFe = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:NFREF_refNFe", nsNfe))
        rEFNF_cUF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNF_cUF", nsNfe))
        rEFNF_AAMM = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNF_AAMM", nsNfe))
        rEFNF_CNPJ = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNF_CNPJ", nsNfe))
        rEFNF_mod = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNF_mod", nsNfe))
        rEFNF_serie = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNF_serie", nsNfe))
        rEFNF_nNF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNF_nNF", nsNfe))
        rEFNFP_cUF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNFP_cUF", nsNfe))
        rEFNFP_AAMM = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNFP_AAMM", nsNfe))
        rEFNFP_CNPJ = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNFP_CNPJ", nsNfe))
        rEFNFP_CPF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNFP_CPF", nsNfe))
        rEFNFP_IE = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNFP_IE", nsNfe))
        rEFNFP_mod = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNFP_mod", nsNfe))
        rEFNFP_serie = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNFP_serie", nsNfe))
        rEFNFP_nNF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFNFP_nNF", nsNfe))
        refCTe = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:refCTe", nsNfe))
        eFECF_mod = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFECF_mod", nsNfe))
        rREFECF_nECF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFECF_nECF", nsNfe))
        rEFECF_nCOO = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:REFECF_nCOO", nsNfe))


#======================================================================== Emitente ============================================================
        emit_CNPJ =       self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:CNPJ", nsNfe))
        emit_CPF =        ''
        emit_xNome =      self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:xNome", nsNfe))
        emit_xFant =      self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:xFant", nsNfe))
        emit_xLgr =       self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:xLgr", nsNfe))
        emit_nro =        self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:nro", nsNfe))
        enderEMIT_xCpl =  self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:xCpl", nsNfe))
        xBairroEmit =     self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:xBairro", nsNfe))
        cMunEmit =        self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:cMun", nsNfe))
        xMunEmit =        self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:xMun", nsNfe))
        UFEmit =          self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:UF", nsNfe))
        CEPEmit =         self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:CEP", nsNfe))
        enderEMIT_cPais = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:xPais", nsNfe))
        enderEMIT_xPais = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:xPais", nsNfe))
        foneEmit =        self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:fone", nsNfe))
        IEemit =          self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:IE", nsNfe))
        iEST =          self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:IEST", nsNfe))
        IMEmit =          self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:IM", nsNfe))
        CNAEEmit =        self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:CNAE", nsNfe))
        CRTEmit =         self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:CRT", nsNfe))


#======================================================================== Destinatário ============================================================
        dest_CNPJ       = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:CNPJ", nsNfe))
        dest_CPF        = ''
        idEstrangeiro   = ''
        dest_xNome      = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:xNome", nsNfe))
        dest_xLgr       = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:xLgr", nsNfe))
        dest_nro        = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:nro", nsNfe))
        destComplemento = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:xCpl", nsNfe))
        dest_xBairro    = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:xBairro", nsNfe))
        cMunDest        = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:cMun", nsNfe))
        xMunDest        = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:xMun", nsNfe))
        uFDest          = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:UF", nsNfe))
        cEPDest         = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:CEP", nsNfe))
        cPaisDest       = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:cPais", nsNfe))
        xPaisDest       = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:xPais", nsNfe))
        enderDEST_fone  = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:enderDest/ns:fone", nsNfe))
        indIEDest       = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:indIEDest", nsNfe))
        iEdest          = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:IE", nsNfe))
        iSUF            = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:ISUF", nsNfe))
        iM              = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:IM", nsNfe))
        email           = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:dest/ns:email", nsNfe))


#================================================================================================== Itens ========================================================
        for item in root.findall('./ns:NFe/ns:infNFe/ns:det', nsNfe):   
            #================/det/prod
                nItem = item.get('nItem')
                cProd = self.check_none(item.find("./ns:prod/ns:cProd", nsNfe))
                cEAN = self.check_none(item.find("./ns:prod/ns:cEAN", nsNfe))
                cBarra = " "
                xProd = self.check_none(item.find("./ns:prod/ns:xProd", nsNfe))
                nCM = self.check_none(item.find("./ns:prod/ns:NCM", nsNfe))
                nVE = " "
                cEST = self.check_none(item.find("./ns:prod/ns:CEST", nsNfe))
                indEscala = " "
                cNPJFab = " "
                cBenef = " "
                eXTIPI = self.check_none(item.find("./ns:prod/ns:EXTIPI", nsNfe))
                cFOP = self.check_none(item.find("./ns:prod/ns:CFOP", nsNfe))
                uCom = self.check_none(item.find("./ns:prod/ns:uCom", nsNfe))
                qCom = self.check_none(item.find("./ns:prod/ns:qCom", nsNfe))
                vUnCom = self.check_none(item.find("./ns:prod/ns:vUnCom", nsNfe))
                vProd = self.check_none(item.find("./ns:prod/ns:vProd", nsNfe))
                cEANTrib = self.check_none(item.find("./ns:prod/ns:cEANTrib", nsNfe))
                cBarraTrib = " "
                uTrib = self.check_none(item.find("./ns:prod/ns:uTrib", nsNfe))
                qTrib = self.check_none(item.find("./ns:prod/ns:qTrib", nsNfe))
                vUnTrib = self.check_none(item.find("./ns:prod/ns:vUnTrib", nsNfe))
                vFrete = self.check_none(item.find("./ns:prod/ns:vFrete", nsNfe))
                vSeg = self.check_none(item.find("./ns:prod/ns:vSeg", nsNfe))
                vDesc = self.check_none(item.find("./ns:prod/ns:vDesc", nsNfe))
                vOutro = self.check_none(item.find("./ns:prod/ns:vOutro", nsNfe))
                indTot = self.check_none(item.find("./ns:prod/ns:indTot", nsNfe))
                dI_nDI = self.check_none(item.find("./ns:prod/ns:DI/ns:nDI", nsNfe))
                dI_dDI = self.check_none(item.find("./ns:prod/ns:DI/ns:dDI", nsNfe))
                dI_xLocDesemb = self.check_none(item.find("./ns:prod/ns:DI/ns:xLocDesemb", nsNfe))
                dI_UFDesemb = self.check_none(item.find("./ns:prod/ns:DI/ns:UFDesemb", nsNfe))
                dI_dDesemb = self.check_none(item.find("./ns:prod/ns:DI/ns:dDesemb", nsNfe))
                dI_tpViaTransp = self.check_none(item.find("./ns:prod/ns:DI/ns:tpViaTransp", nsNfe))
                dI_vAFRMM = self.check_none(item.find("./ns:prod/ns:DI/ns:vAFRMM", nsNfe))
                dI_tpIntermedio = self.check_none(item.find("./ns:prod/ns:DI/ns:tpIntermedio", nsNfe))
                dI_CNPJ = self.check_none(item.find("./ns:prod/ns:DI/ns:CNPJ", nsNfe))
                dI_UFTerceiro = self.check_none(item.find("./ns:prod/ns:DI/ns:UFTerceiro", nsNfe))
                dI_cExportador = self.check_none(item.find("./ns:prod/ns:DI/ns:cExportador", nsNfe))
                aDI_nAdicao = self.check_none(item.find("./ns:prod/ns:DI/ns:adi/ns:nAdicao", nsNfe))
                aDI_nSeqAdic = self.check_none(item.find("./ns:prod/ns:DI/ns:adi/ns:nSeqAdic", nsNfe))
                aDI_cFabricante = self.check_none(item.find("./ns:prod/ns:DI/ns:adi/ns:cFabricante", nsNfe))
                aDI_vDescDI = self.check_none(item.find("./ns:prod/ns:DI/ns:adi/ns:vDescDI", nsNfe))
                aDI_nDraw = self.check_none(item.find("./ns:prod/ns:DI/ns:adi/ns:nDraw", nsNfe))
                dETEXPORT_nDraw = " "
                eXPORTIND_nRE = " "
                eXPORTIND_chNFe = " "
                eXPORTIND_qExport = " "
                xPed = self.check_none(item.find("./ns:prod/ns:xPed", nsNfe))
                nItemPed = self.check_none(item.find("./ns:prod/ns:nItemPed", nsNfe))
                nFCI = self.check_none(item.find("./ns:prod/ns:nFCI", nsNfe))
                rASTRO_nLote = self.check_none(item.find("./ns:prod/ns:rastro/ns:nLote", nsNfe))
                rASTRO_qLote = self.check_none(item.find("./ns:prod/ns:rastro/ns:qLote", nsNfe))
                rASTRO_dFab = self.check_none(item.find("./ns:prod/ns:rastro/ns:dFab", nsNfe))
                rASTRO_dVal = self.check_none(item.find("./ns:prod/ns:rastro/ns:dVal", nsNfe))
                rASTRO_cAgreg = self.check_none(item.find("./ns:prod/ns:rastro/ns:cAgreg", nsNfe))
                iNFPRODNFF_cProdFisco = " "
                iNFPRODNFF_cOperNFF = " "
                iNFPRODEMB_xEmb = " "
                iNFPRODEMB_qVolEmb = " "
                iNFPRODEMB_uEmb = " "
                vEICPROD_tpOp = self.check_none(item.find("./ns:prod/ns:veicProd/ns:tpOp", nsNfe))
                vEICPROD_chassi = self.check_none(item.find("./ns:prod/ns:veicProd/ns:chassi", nsNfe))
                vEICPROD_cCor = self.check_none(item.find("./ns:prod/ns:veicProd/ns:cCor", nsNfe))
                vEICPROD_xCor = self.check_none(item.find("./ns:prod/ns:veicProd/ns:xCor", nsNfe))
                vEICPROD_pot = self.check_none(item.find("./ns:prod/ns:veicProd/ns:pot", nsNfe))
                vEICPROD_cilin = self.check_none(item.find("./ns:prod/ns:veicProd/ns:cilin", nsNfe))
                vEICPROD_pesoL = self.check_none(item.find("./ns:prod/ns:veicProd/ns:pesoL", nsNfe))
                vEICPROD_pesoB = self.check_none(item.find("./ns:prod/ns:veicProd/ns:pesoB", nsNfe))
                vEICPROD_nSerie = self.check_none(item.find("./ns:prod/ns:veicProd/ns:nSerie", nsNfe))
                vEICPROD_tpComb = self.check_none(item.find("./ns:prod/ns:veicProd/ns:tpComb", nsNfe))
                vEICPROD_nMotor = self.check_none(item.find("./ns:prod/ns:veicProd/ns:nMotor", nsNfe))
                vEICPROD_CMT = self.check_none(item.find("./ns:prod/ns:veicProd/ns:CMT", nsNfe))
                vEICPROD_dist = self.check_none(item.find("./ns:prod/ns:veicProd/ns:dist", nsNfe))
                vEICPROD_anoMod = self.check_none(item.find("./ns:prod/ns:veicProd/ns:anoMod", nsNfe))
                vEICPROD_anoFab = self.check_none(item.find("./ns:prod/ns:veicProd/ns:anoFab", nsNfe))
                vEICPROD_tpPint = self.check_none(item.find("./ns:prod/ns:veicProd/ns:tpPint", nsNfe))
                vEICPROD_tpVeic = self.check_none(item.find("./ns:prod/ns:veicProd/ns:tpVeic", nsNfe))
                vEICPROD_espVeic = self.check_none(item.find("./ns:prod/ns:veicProd/ns:espVeic", nsNfe))
                vEICPROD_VIN = self.check_none(item.find("./ns:prod/ns:veicProd/ns:VIN", nsNfe))
                vEICPROD_condVeic = self.check_none(item.find("./ns:prod/ns:veicProd/ns:condVeic", nsNfe))
                vEICPROD_cMod = self.check_none(item.find("./ns:prod/ns:veicProd/ns:cMod", nsNfe))
                vEICPROD_cCorDENATRAN = self.check_none(item.find("./ns:prod/ns:veicProd/ns:RENAVAM", nsNfe))
                vEICPROD_lota = self.check_none(item.find("./ns:prod/ns:veicProd/ns:lota", nsNfe))
                vEICPROD_tpRest = self.check_none(item.find("./ns:prod/ns:veicProd/ns:tpRest", nsNfe))
                mED_nLote = self.check_none(item.find("./ns:prod/ns:med/ns:nLote", nsNfe))
                mED_qLote = self.check_none(item.find("./ns:prod/ns:med/ns:qLote", nsNfe))
                mED_dFab = self.check_none(item.find("./ns:prod/ns:med/ns:dFab", nsNfe))
                mED_dVal = self.check_none(item.find("./ns:prod/ns:med/ns:dVal", nsNfe))
                mED_vPMC = self.check_none(item.find("./ns:prod/ns:med/ns:vPMC", nsNfe))
                mED_cProdANVISA = self.check_none(item.find("./ns:prod/ns:med/ns:cProdANVISA", nsNfe))
                mED_xMotivoIsencao = self.check_none(item.find("./ns:prod/ns:med/ns:xMotivoIsencao", nsNfe))
                aRMA_tpArma = self.check_none(item.find("./ns:prod/ns:arma/ns:tpArma", nsNfe))
                aRMA_nSerie = self.check_none(item.find("./ns:prod/ns:arma/ns:nSerie", nsNfe))
                aRMA_nCano = self.check_none(item.find("./ns:prod/ns:arma/ns:nCano", nsNfe))
                aRMA_descr = self.check_none(item.find("./ns:prod/ns:arma/ns:descr", nsNfe))
                cOMB_cProdANP = self.check_none(item.find("./ns:prod/ns:comb/ns:cProdANP", nsNfe))
                cOMB_descANP = self.check_none(item.find("./ns:prod/ns:comb/ns:descANP", nsNfe))
                cOMB_pGLP = self.check_none(item.find("./ns:prod/ns:comb/ns:pGLP", nsNfe))
                cOMB_pGNn = self.check_none(item.find("./ns:prod/ns:comb/ns:pGNn", nsNfe))
                cOMB_pGNi = self.check_none(item.find("./ns:prod/ns:comb/ns:pGNi", nsNfe))
                cOMB_vPart = self.check_none(item.find("./ns:prod/ns:comb/ns:vPart", nsNfe))
                cOMB_pMixGN = self.check_none(item.find("./ns:prod/ns:comb/ns:pMixGN", nsNfe))
                cOMB_CODIF = self.check_none(item.find("./ns:prod/ns:comb/ns:CODIF", nsNfe))
                cOMB_qTemp = self.check_none(item.find("./ns:prod/ns:comb/ns:qTemp", nsNfe))
                cOMB_UFCons = self.check_none(item.find("./ns:prod/ns:comb/ns:UFCons", nsNfe))
                cIDE_qBCProd = " "
                cIDE_vAliqProd = " "
                cIDE_vCIDE = " "
                eNCERRANTE_nBico = self.check_none(item.find("./ns:prod/ns:encerrante/ns:nBico", nsNfe))
                eNCERRANTE_nBomba = self.check_none(item.find("./ns:prod/ns:encerrante/ns:nBomba", nsNfe))
                eNCERRANTE_nTanque = self.check_none(item.find("./ns:prod/ns:encerrante/ns:nTanque", nsNfe))
                eNCERRANTE_vEncIni = self.check_none(item.find("./ns:prod/ns:encerrante/ns:vEncIni", nsNfe))
                eNCERRANTE_vEncFin = self.check_none(item.find("./ns:prod/ns:encerrante/ns:vEncFin", nsNfe))
                pBio = self.check_none(item.find("./ns:prod/ns:pBio", nsNfe))
                oRIGCOMB_indImport = " "
                oRIGCOMB_cUFOrig = " "
                oRIGCOMB_pOrig = " "
                nRECOPI = " "
                iMPOSTO_vTotTrib = self.check_none(item.find("./ns:imposto/ns:vTotTrib", nsNfe))
                tipo_ICMS = " "
                iCMS_orig = " "
                iCMS_CSOSN = " "
                iCMS_pCredSN = " "
                iCMS_vCredICMSSN = " "
                iCMS_CST = " "
                iCMS_vBCSTRet = " "
                iCMS_vICMSSTRet = " "
                iCMS_vBCSTDest = " "
                iCMS_vICMSSTDest = " "
                iCMS_modBC = " "
                iCMS_modBCST = " "
                iCMS_pRedBC = " "
                iCMS_vBC = " "
                iCMS_pICMS = " "
                iCMS_vICMSOp = " "
                iCMS_pDif = " "
                iCMS_vICMSDif = " "
                iCMS_vICMS = " "
                iCMS_vICMSDeson = " "
                iCMS_motDesICMS = " "
                iCMS_pMVAST = " "
                iCMS_pRedBCST = " "
                iCMS_vBCST = " "
                iCMS_pICMSST = " "
                iCMS_vICMSST = " "
                iCMS_pBCOp = " "
                iCMS_UFST = " "
                iCMS_pFCP = " "
                iCMS_vFCP = " "
                iCMS_vBCFCP = " "
                iCMS_pFCPST = " "
                iCMS_vFCPST = " "
                iCMS_vBCFCPST = " "
                iCMS_pFCPSTRet = " "
                iCMS_vFCPSTRet = " "
                iCMS_vBCFCPSTRet = " "
                iCMS_pRedBCEfet = " "
                iCMS_vBCEfet = " "
                iCMS_pICMSEfet = " "
                iCMS_vICMSEfet = " "
                iCMS_pST = " "
                iCMS_qBCMono = " "
                iCMS_adRemICMS = " "
                iCMS_vICMSMono = " "
                iCMS_qBCMonoReten = " "
                iCMS_adRemICMSReten = " "
                iCMS_vICMSMonoReten = " "
                iCMS_pRedAdRem = " "
                iCMS_motRedAdRem = " "
                iCMS_motDesICMSST = " "
                iCMS_pFCPDif = " "
                iCMS_vFCPDif = " "
                iCMS_vFCPEfet = " "
                iCMS_vICMSMonoOp = " "
                iCMS_vICMSMonoDif = " "
                iCMS_qBCMonoDif = " "
                iCMS_adRemICMSDif = " "
                iCMS_vICMSSubstituto = " "
                iCMS_qBCMonoRet = " "
                iCMS_adRemICMSRet = " "
                iCMS_vICMSMonoRet = " "
                vazio = " "
                iPI_clEnq = self.check_none(item.find("./ns:imposto/ns:IPI/ns:clEnq", nsNfe))
                iPI_CNPJProd = self.check_none(item.find("./ns:imposto/ns:IPI/ns:CNPJProd", nsNfe))
                iPI_cSelo = self.check_none(item.find("./ns:imposto/ns:IPI/ns:cSelo", nsNfe))
                iPI_qSelo = self.check_none(item.find("./ns:imposto/ns:IPI/ns:qSelo", nsNfe))
                iPI_cEnq = self.check_none(item.find("./ns:imposto/ns:IPI/ns:cEnq", nsNfe))
                iPITRIB_CST = " "
                iPITRIB_vBC = " "
                iPITRIB_pIPI = self.check_none(item.find("./ns:imposto/ns:IPI/ns:IPITrib/ns:pIPI", nsNfe))
                iPITRIB_qUnid = " "
                iPITRIB_vUnid = " "
                iPITRIB_vIPI = self.check_none(item.find("./ns:imposto/ns:IPI/ns:IPITrib/ns:vIPI", nsNfe))
                iPINT_CST = " "
                iI_vBC = self.check_none(item.find("./ns:imposto/ns:II/ns:vBC", nsNfe))
                iI_vDespAdu = self.check_none(item.find("./ns:imposto/ns:II/ns:vDespAdu", nsNfe))
                iI_vII = self.check_none(item.find("./ns:imposto/ns:II/ns:vII", nsNfe))
                iI_vIOF = self.check_none(item.find("./ns:imposto/ns:II/ns:vIOF", nsNfe))
                iSSQN_vBC = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:vBC", nsNfe))
                iSSQN_vAliq = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:vAliq", nsNfe))
                iSSQN_vISSQN = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:vISSQN", nsNfe))
                iSSQN_cMunFG = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:cMunFG", nsNfe))
                iSSQN_cListServ = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:cListServ", nsNfe))
                iSSQN_vDeducao = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:vDeducao", nsNfe))
                iSSQN_vOutro = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:vOutro", nsNfe))
                iSSQN_vDescIncond = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:vDescIncond", nsNfe))
                iSSQN_vDescCond = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:vDescCond", nsNfe))
                iSSQN_vISSRet = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:vISSRet", nsNfe))
                iSSQN_indISS = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:indISS", nsNfe))
                iSSQN_cServico = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:cServico", nsNfe))
                iSSQN_cMun = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:cMun", nsNfe))
                iSSQN_cPais = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:cPais", nsNfe))
                iSSQN_nProcesso = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:nProcesso", nsNfe))
                iSSQN_indIncentivo = self.check_none(item.find("./ns:imposto/ns:ISSQN/ns:indIncentivo", nsNfe))
                tipo_PIS = " "
                pIS_CST = " "
                pIS_vBC = " "
                pIS_pPIS = " "
                pIS_vPIS = " "
                pIS_qBCProd = " "
                pIS_vAliqProd = " "
                tipo_COFINS = " "
                cOFINS_CST = " "
                cOFINS_vBC = " "
                cOFINS_pCOFINS = " "
                cOFINS_vCOFINS = " "
                cOFINS_qBCProd = " "
                cOFINS_vAliqProd = " "
                iCMSUFDEST_vBCUFDest = " "
                iCMSUFDEST_vBCFCPUFDest = " "
                iCMSUFDEST_pFCPUFDest = " "
                iCMSUFDEST_pICMSUFDest = " "
                iCMSUFDEST_pICMSInter = " "
                iCMSUFDEST_pICMSInterPart = " "
                iCMSUFDEST_vFCPUFDest = " "
                iCMSUFDEST_vICMSUFDest = " "
                iCMSUFDEST_vICMSUFRemet = " "
                iMPOSTODEVOL_pDevol = self.check_none(item.find("./ns:impostoDevol/ns:pDevol", nsNfe))
                iMPOSTODEVOL_vIPIDevol = self.check_none(item.find("./ns:impostoDevol/ns:vIPIDevol", nsNfe))
                infAdProd = self.check_none(item.find("./ns:infAdProd", nsNfe))
                oBSITEM_obsCont_xTexto = " "
                oBSITEM_obsCont_xCampo = " "
                oBSITEM_obsFisco_xTexto = " "
                oBSITEM_obsFisco_xCampo = " "


        itens_data = {"Arquivo": chave,"nNF": nNF, "NumItem": nItem, "cProd": cProd, "cEAN": cEAN, "cBarra": cBarra, "xProd": xProd, "NCM": nCM, "NVE": nVE, 
                      "CEST": cEST, "indEscala": indEscala, "CNPJFab": cNPJFab, "cBenef": cBenef, "EXTIPI": eXTIPI, "CFOP": cFOP, "uCom": uCom, "qCom": qCom, 
                      "vUnCom": vUnCom, "vProd": vProd, "cEANTrib": cEANTrib, "cBarraTrib": cBarraTrib, "uTrib": uTrib, "qTrib": qTrib, "vUnTrib": vUnTrib, 
                      "vFrete": vFrete, "vSeg": vSeg, "vDesc": vDesc, "vOutro": vOutro, "indTot": indTot, "DI_nDI": dI_nDI, "DI_dDI": dI_dDI, "DI_xLocDesemb": dI_xLocDesemb, 
                      "DI_UFDesemb": dI_UFDesemb, "DI_dDesemb": dI_dDesemb, "DI_tpViaTransp": dI_tpViaTransp, "DI_vAFRMM": dI_vAFRMM, "DI_tpIntermedio": dI_tpIntermedio, 
                      "DI_CNPJ": dI_CNPJ, "DI_UFTerceiro": dI_UFTerceiro, "DI_cExportador": dI_cExportador, "ADI_nAdicao": aDI_nAdicao, "ADI_nSeqAdic": aDI_nSeqAdic, 
                      "ADI_cFabricante": aDI_cFabricante, "ADI_vDescDI": aDI_vDescDI, "ADI_nDraw": aDI_nDraw, "DETEXPORT_nDraw": dETEXPORT_nDraw, "EXPORTIND_nRE": eXPORTIND_nRE, 
                      "EXPORTIND_chNFe": eXPORTIND_chNFe, "EXPORTIND_qExport": eXPORTIND_qExport, "xPed": xPed, "nItemPed": nItemPed, "nFCI": nFCI, "RASTRO_nLote": rASTRO_nLote, "RASTRO_qLote": rASTRO_qLote, "RASTRO_dFab": rASTRO_dFab, "RASTRO_dVal": rASTRO_dVal, "RASTRO_cAgreg": rASTRO_cAgreg, "INFPRODNFF_cProdFisco": iNFPRODNFF_cProdFisco, "INFPRODNFF_cOperNFF": iNFPRODNFF_cOperNFF, "INFPRODEMB_xEmb": iNFPRODEMB_xEmb, "INFPRODEMB_qVolEmb": iNFPRODEMB_qVolEmb, "INFPRODEMB_uEmb": iNFPRODEMB_uEmb, "VEICPROD_tpOp": vEICPROD_tpOp, "VEICPROD_chassi": vEICPROD_chassi, "VEICPROD_cCor": vEICPROD_cCor, "VEICPROD_xCor": vEICPROD_xCor, "VEICPROD_pot": vEICPROD_pot, "VEICPROD_cilin": vEICPROD_cilin, "VEICPROD_pesoL": vEICPROD_pesoL, "VEICPROD_pesoB": vEICPROD_pesoB, "VEICPROD_nSerie": vEICPROD_nSerie, "VEICPROD_tpComb": vEICPROD_tpComb, "VEICPROD_nMotor": vEICPROD_nMotor, "VEICPROD_CMT": vEICPROD_CMT, "VEICPROD_dist": vEICPROD_dist, "VEICPROD_anoMod": vEICPROD_anoMod, "VEICPROD_anoFab": vEICPROD_anoFab, "VEICPROD_tpPint": vEICPROD_tpPint, "VEICPROD_tpVeic": vEICPROD_tpVeic, "VEICPROD_espVeic": vEICPROD_espVeic, "VEICPROD_VIN": vEICPROD_VIN, "VEICPROD_condVeic": vEICPROD_condVeic, "VEICPROD_cMod": vEICPROD_cMod, "VEICPROD_cCorDENATRAN": vEICPROD_cCorDENATRAN, "VEICPROD_lota": vEICPROD_lota, "VEICPROD_tpRest": vEICPROD_tpRest, "MED_nLote": mED_nLote, "MED_qLote": mED_qLote, "MED_dFab": mED_dFab, "MED_dVal": mED_dVal, "MED_vPMC": mED_vPMC, "MED_cProdANVISA": mED_cProdANVISA, "MED_xMotivoIsencao": mED_xMotivoIsencao, "ARMA_tpArma": aRMA_tpArma, "ARMA_nSerie": aRMA_nSerie, "ARMA_nCano": aRMA_nCano, "ARMA_descr": aRMA_descr, "COMB_cProdANP": cOMB_cProdANP, "COMB_descANP": cOMB_descANP, "COMB_pGLP": cOMB_pGLP, "COMB_pGNn": cOMB_pGNn, "COMB_pGNi": cOMB_pGNi, "COMB_vPart": cOMB_vPart, "COMB_pMixGN": cOMB_pMixGN, "COMB_CODIF": cOMB_CODIF, "COMB_qTemp": cOMB_qTemp, "COMB_UFCons": cOMB_UFCons, "CIDE_qBCProd": cIDE_qBCProd, "CIDE_vAliqProd": cIDE_vAliqProd, "CIDE_vCIDE": cIDE_vCIDE, "ENCERRANTE_nBico": eNCERRANTE_nBico, "ENCERRANTE_nBomba": eNCERRANTE_nBomba, "ENCERRANTE_nTanque": eNCERRANTE_nTanque, "ENCERRANTE_vEncIni": eNCERRANTE_vEncIni, "ENCERRANTE_vEncFin": eNCERRANTE_vEncFin, "pBio": pBio, "ORIGCOMB_indImport": oRIGCOMB_indImport, "ORIGCOMB_cUFOrig": oRIGCOMB_cUFOrig, "ORIGCOMB_pOrig": oRIGCOMB_pOrig, "nRECOPI": nRECOPI, "IMPOSTO_vTotTrib": iMPOSTO_vTotTrib, "Tipo_ICMS": tipo_ICMS, "ICMS_orig": iCMS_orig, "ICMS_CSOSN": iCMS_CSOSN, "ICMS_pCredSN": iCMS_pCredSN, "ICMS_vCredICMSSN": iCMS_vCredICMSSN, "ICMS_CST": iCMS_CST, "ICMS_vBCSTRet": iCMS_vBCSTRet, "ICMS_vICMSSTRet": iCMS_vICMSSTRet, "ICMS_vBCSTDest": iCMS_vBCSTDest, "ICMS_vICMSSTDest": iCMS_vICMSSTDest, "ICMS_modBC": iCMS_modBC, "ICMS_modBCST": iCMS_modBCST, "ICMS_pRedBC": iCMS_pRedBC, "ICMS_vBC": iCMS_vBC, "ICMS_pICMS": iCMS_pICMS, "ICMS_vICMSOp": iCMS_vICMSOp, "ICMS_pDif": iCMS_pDif, "ICMS_vICMSDif": iCMS_vICMSDif, "ICMS_vICMS": iCMS_vICMS, "ICMS_vICMSDeson": iCMS_vICMSDeson, "ICMS_motDesICMS": iCMS_motDesICMS, "ICMS_pMVAST": iCMS_pMVAST, "ICMS_pRedBCST": iCMS_pRedBCST, "ICMS_vBCST": iCMS_vBCST, "ICMS_pICMSST": iCMS_pICMSST, "ICMS_vICMSST": iCMS_vICMSST, "ICMS_pBCOp": iCMS_pBCOp, "ICMS_UFST": iCMS_UFST, "ICMS_pFCP": iCMS_pFCP, "ICMS_vFCP": iCMS_vFCP, "ICMS_vBCFCP": iCMS_vBCFCP, "ICMS_pFCPST": iCMS_pFCPST, "ICMS_vFCPST": iCMS_vFCPST, "ICMS_vBCFCPST": iCMS_vBCFCPST, "ICMS_pFCPSTRet": iCMS_pFCPSTRet, "ICMS_vFCPSTRet": iCMS_vFCPSTRet, "ICMS_vBCFCPSTRet": iCMS_vBCFCPSTRet, "ICMS_pRedBCEfet": iCMS_pRedBCEfet, "ICMS_vBCEfet": iCMS_vBCEfet, "ICMS_pICMSEfet": iCMS_pICMSEfet, "ICMS_vICMSEfet": iCMS_vICMSEfet, "ICMS_pST": iCMS_pST, "ICMS_qBCMono": iCMS_qBCMono, "ICMS_adRemICMS": iCMS_adRemICMS, "ICMS_vICMSMono": iCMS_vICMSMono, "ICMS_qBCMonoReten": iCMS_qBCMonoReten, "ICMS_adRemICMSReten": iCMS_adRemICMSReten, "ICMS_vICMSMonoReten": iCMS_vICMSMonoReten, "ICMS_pRedAdRem": iCMS_pRedAdRem, "ICMS_motRedAdRem": iCMS_motRedAdRem, "ICMS_motDesICMSST": iCMS_motDesICMSST, "ICMS_pFCPDif": iCMS_pFCPDif, "ICMS_vFCPDif": iCMS_vFCPDif, "ICMS_vFCPEfet": iCMS_vFCPEfet, "ICMS_vICMSMonoOp": iCMS_vICMSMonoOp, "ICMS_vICMSMonoDif": iCMS_vICMSMonoDif, "ICMS_qBCMonoDif": iCMS_qBCMonoDif, "ICMS_adRemICMSDif": iCMS_adRemICMSDif, "ICMS_vICMSSubstituto": iCMS_vICMSSubstituto, "ICMS_qBCMonoRet": iCMS_qBCMonoRet, "ICMS_adRemICMSRet": iCMS_adRemICMSRet, "ICMS_vICMSMonoRet": iCMS_vICMSMonoRet, "vazio": vazio, "IPI_clEnq": iPI_clEnq, "IPI_CNPJProd": iPI_CNPJProd, "IPI_cSelo": iPI_cSelo, "IPI_qSelo": iPI_qSelo, "IPI_cEnq": iPI_cEnq, "IPITRIB_CST": iPITRIB_CST, "IPITRIB_vBC": iPITRIB_vBC, "IPITRIB_pIPI": iPITRIB_pIPI, "IPITRIB_qUnid": iPITRIB_qUnid, "IPITRIB_vUnid": iPITRIB_vUnid, "IPITRIB_vIPI": iPITRIB_vIPI, "IPINT_CST": iPINT_CST, "II_vBC": iI_vBC, "II_vDespAdu": iI_vDespAdu, "II_vII": iI_vII, "II_vIOF": iI_vIOF, "ISSQN_vBC": iSSQN_vBC, "ISSQN_vAliq": iSSQN_vAliq, "ISSQN_vISSQN": iSSQN_vISSQN, "ISSQN_cMunFG": iSSQN_cMunFG, "ISSQN_cListServ": iSSQN_cListServ, "ISSQN_vDeducao": iSSQN_vDeducao, "ISSQN_vOutro": iSSQN_vOutro, "ISSQN_vDescIncond": iSSQN_vDescIncond, "ISSQN_vDescCond": iSSQN_vDescCond, "ISSQN_vISSRet": iSSQN_vISSRet, "ISSQN_indISS": iSSQN_indISS, "ISSQN_cServico": iSSQN_cServico, "ISSQN_cMun": iSSQN_cMun, "ISSQN_cPais": iSSQN_cPais, "ISSQN_nProcesso": iSSQN_nProcesso, "ISSQN_indIncentivo": iSSQN_indIncentivo, "Tipo_PIS": tipo_PIS, "PIS_CST": pIS_CST, "PIS_vBC": pIS_vBC, "PIS_pPIS": pIS_pPIS, "PIS_vPIS": pIS_vPIS, "PIS_qBCProd": pIS_qBCProd, "PIS_vAliqProd": pIS_vAliqProd, "Tipo_COFINS": tipo_COFINS, "COFINS_CST": cOFINS_CST, "COFINS_vBC": cOFINS_vBC, "COFINS_pCOFINS": cOFINS_pCOFINS, "COFINS_vCOFINS": cOFINS_vCOFINS, "COFINS_qBCProd": cOFINS_qBCProd, "COFINS_vAliqProd": cOFINS_vAliqProd, "ICMSUFDEST_vBCUFDest": iCMSUFDEST_vBCUFDest, "ICMSUFDEST_vBCFCPUFDest": iCMSUFDEST_vBCFCPUFDest, "ICMSUFDEST_pFCPUFDest": iCMSUFDEST_pFCPUFDest, "ICMSUFDEST_pICMSUFDest": iCMSUFDEST_pICMSUFDest, "ICMSUFDEST_pICMSInter": iCMSUFDEST_pICMSInter, "ICMSUFDEST_pICMSInterPart": iCMSUFDEST_pICMSInterPart, "ICMSUFDEST_vFCPUFDest": iCMSUFDEST_vFCPUFDest, "ICMSUFDEST_vICMSUFDest": iCMSUFDEST_vICMSUFDest, "ICMSUFDEST_vICMSUFRemet": iCMSUFDEST_vICMSUFRemet, "IMPOSTODEVOL_pDevol": iMPOSTODEVOL_pDevol, "IMPOSTODEVOL_vIPIDevol": iMPOSTODEVOL_vIPIDevol, "infAdProd": infAdProd, "OBSITEM_obsCont_xTexto": oBSITEM_obsCont_xTexto, "OBSITEM_obsCont_xCampo": oBSITEM_obsCont_xCampo, "OBSITEM_obsFisco_xTexto": oBSITEM_obsFisco_xTexto, "OBSITEM_obsFisco_xCampo": oBSITEM_obsFisco_xCampo



                        }
        dados["Itens"].append(itens_data)

#============================================================================================ TOTAL IMPOSTOS ==========================================================
        #Extraindo informações do 'ICMSTot'
        vBC = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vBC", nsNfe))
        vICMS = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vICMS", nsNfe))
        vICMSDeson = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vICMSDeson", nsNfe))
        vFCPUFDest = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vFCPUFDest", nsNfe))
        vICMSUFDest = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vICMSUFDest", nsNfe))
        vICMSUFRemet = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vICMSUFRemet", nsNfe))
        vFCP = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vFCP", nsNfe))
        vBCST = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vBCST", nsNfe))
        vST = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vST", nsNfe))
        vFCPST = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vFCPST", nsNfe))
        vFCPSTRet = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vFCPSTRet", nsNfe))
        vProd = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vProd", nsNfe))
        vFrete = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vFrete", nsNfe))
        vSeg = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vSeg", nsNfe))
        vDesc = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vDesc", nsNfe))
        vII = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vII", nsNfe))
        vIPI = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vIPI", nsNfe))
        vIPIDevol = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vIPIDevol", nsNfe))
        vPIS = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vPIS", nsNfe))
        vCOFINS = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vCOFINS", nsNfe))
        vOutro = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vOutro", nsNfe))
        vNF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vNF", nsNfe))
        vTotTrib = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vTotTrib", nsNfe))

#============================================================================================ TRANSPORTE ===================================================================
        # Extraindo informações da seção 'TRANSPORTE'
        transp_modFrete = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:transp/ns:modFrete", nsNfe))
        # Extraindo informações da seção 'TRANSPORTE-TRANSPORTADORA'
        transp_CNPJ = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:transp/ns:transporta/ns:CNPJ", nsNfe))
        transp_xNome = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:transp/ns:transporta/ns:xNome", nsNfe))
        transp_IE = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:transp/ns:transporta/ns:IE", nsNfe))
        transp_xEnder = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:transp/ns:transporta/ns:xEnder", nsNfe))
        transp_xMun = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:transp/ns:transporta/ns:xMun", nsNfe))
        transp_UF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:transp/ns:transporta/ns:UF", nsNfe))
        # Extraindo informações da seção 'TRANSPORTE-VOLUME'
        transp_esp = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:transp/ns:vol/ns:esp", nsNfe))
        transp_pesoL = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:transp/ns:vol/ns:pesoL", nsNfe))
        transp_pesoB = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:transp/ns:vol/ns:pesoB", nsNfe))

#============================================================================================ PAGAMENTO ===================================================================
        # Extraindo informações da seção 'pag-detPag'
        pag_tPag = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:pag/ns:detPag/ns:tPag", nsNfe))
        pag_vPag = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:pag/ns:detPag/ns:vPag", nsNfe))

#============================================================================================ INFO ADICIONAIS =============================================================
        # Extraindo informações da seção 'infAdic'
        infAdFisco = ''
        infCpl = ''
        OBSCONT_xCampo = ''
        OBSCONT_xTexto = ''
        OBSFISCO_xCampo = ''
        OBSFISCO_xTexto = ''
        PROCREF_nProc = ''
        PROCREF_indProc = ''
        PROCREF_tpAto = ''

#============================================================================================ Assinatura  ===================================================================
        # Extraindo informações da seção 'Signature '
        DigestValue = ''
        SignatureValue = ''
        X509Certificate = ''

#============================================================================================ Protocolo
        tpAmb = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:tpAmb", nsNfe))
        verAplic = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:verAplic", nsNfe))
        chNFe = self.check_none(root.find("./ns:protNFe/ns:infProt/ns:chNFe", nsNfe))    
        dhRecbto = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:dhRecbto", nsNfe))
        nProt = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:nProt", nsNfe))
        digVal = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:digVal", nsNfe))
        cStat = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:cStat", nsNfe))
        xMotivo = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:xMotivo", nsNfe))


#==========================================================================     DADOS       ============================================================================
        # Adicionando os dados coletados ao dicionário de dados
        dados["Identificação NFE"].append({ "Arquivo": chave, "Versão_XML":versao_XML, "Chave_de_Acesso": arquivo, "cUF": cUF, "cNF": cNF, "natOp": natOp,
                                            "indPag": indPag, "mod": mod, "serie": serie, "nNF": nNF, "dhEmi": dhEmi, "dhSaiEnt": dhSaiEnt,
                                            "hSaiEnt": hSaiEnt, "tpNF": tpNF, "idDest": idDest, "cMunFG": cMunFG, "tpImp": tpImp, "tpEmis": tpEmis,
                                            "cDV": cDV, "tpAmb": tpAmb, "finNFe": finNFe, "indFinal": indFinal, "indPres": indPres, "indIntermed": indIntermed,
                                            "procEmi": procEmi, "verProc": verProc, "dhCont": dhCont, "xJust": xJust, "NFREF_refNFe": nFREF_refNFe,
                                            "REFNF_cUF": rEFNF_cUF, "REFNF_AAMM": rEFNF_AAMM, "REFNF_CNPJ": rEFNF_CNPJ, "REFNF_mod": rEFNF_mod,
                                            "REFNF_serie": rEFNF_serie, "REFNF_nNF": rEFNF_nNF, "REFNFP_cUF": rEFNFP_cUF, "REFNFP_AAMM": rEFNFP_AAMM,
                                            "REFNFP_CNPJ": rEFNFP_CNPJ, "REFNFP_CPF": rEFNFP_CPF, "REFNFP_IE": rEFNFP_IE, "REFNFP_mod": rEFNFP_mod,
                                            "REFNFP_serie": rEFNFP_serie, "REFNFP_nNF": rEFNFP_nNF, "refCTe": refCTe, "REFECF_mod": eFECF_mod,
                                            "REFECF_nECF": rREFECF_nECF, "REFECF_nCOO": rEFECF_nCOO
                                            })

        dados["Emitente"].append({  "Arquivo": chave,"nNF": nNF,"CNPJ": emit_CNPJ, "CPF": emit_CPF, "xNome": emit_xNome, "xFant": emit_xFant,
                                    "enderEMIT_xLgr": emit_xLgr, "enderEMIT_nro": emit_nro, "enderEMIT_xCpl": enderEMIT_xCpl,
                                    "enderEMIT_xBairro": xBairroEmit, "enderEMIT_cMun": cMunEmit, "enderEMIT_xMun": xMunEmit,
                                    "enderEMIT_UF": UFEmit, "enderEMIT_CEP": CEPEmit, "enderEMIT_cPais": enderEMIT_cPais,
                                    "enderEMIT_xPais": enderEMIT_xPais, "enderEMIT_fone": foneEmit, "IE": IEemit, "IEST": iEST,
                                    "IM": IMEmit, "CNAE": CNAEEmit, "CRT": CRTEmit
                                    })

        dados["Destinatário"].append({  "Arquivo": chave,"nNF": nNF,"CNPJ": dest_CNPJ, "CPF": dest_CPF, "idEstrangeiro": idEstrangeiro, "xNome": dest_xNome, 
                                        "enderDEST_xLgr": dest_xLgr, "enderDEST_nro": dest_nro, "enderDEST_xCpl": destComplemento, "enderDEST_xBairro": dest_xBairro, 
                                        "enderDEST_cMun": cMunDest, "enderDEST_xMun": xMunDest, "enderDEST_UF": uFDest, "enderDEST_CEP": cEPDest, "enderDEST_cPais": cPaisDest,
                                        "enderDEST_xPais": xPaisDest, "enderDEST_fone": enderDEST_fone, "indIEDest": indIEDest, "IE": iEdest,
                                        "ISUF": iSUF, "IM": iM, "email": email
                                        })
        
        dados["Total"].append({ "Arquivo": chave,"nNF": nNF, "vBC": vBC,  "vICMS": vICMS,  "vICMSDeson": vICMSDeson, "vFCPUFDest": vFCPUFDest,  
                                "vICMSUFDest": vICMSUFDest,  "vICMSUFRemet": vICMSUFRemet,  "vFCP": vFCP,  "vBCST": vBCST,  
                                "vST": vST,  "vFCPST": vFCPST,  "vFCPSTRet": vFCPSTRet,  "vProd": vProd,  "vFrete": vFrete,  
                                "vSeg": vSeg,  "vDesc": vDesc,  "vII": vII,  "vIPI": vIPI,  "vIPIDevol": vIPIDevol,  
                                "vPIS": vPIS,  "vCOFINS": vCOFINS,  "vOutro": vOutro,  "vNF": vNF,  "vTotTrib": vTotTrib,
                                })
        
        dados["Transportadora"].append({    "Arquivo": chave,"nNF": nNF, "transp_modFrete": transp_modFrete, "transp_CNPJ": transp_CNPJ, "transp_xNome": transp_xNome,
                                            "transp_IE": transp_IE,	"transp_xEnder": transp_xEnder,	"transp_xMun": transp_xMun,	
                                            "transp_UF": transp_UF,	"transp_esp": transp_esp,	"transp_pesoL": transp_pesoL,	
                                            "transp_pesoB": transp_pesoB
                                        })

        dados["Pagamento"].append({ "Arquivo": chave,"nNF": nNF, "pag_tPag": pag_tPag, "pag_vPag": pag_vPag})


        dados["Inf. Adicional"].append({"Arquivo": chave,"nNF": nNF, "infAdFisco": infAdFisco, "infCpl": infCpl, "OBSCONT_xCampo": OBSCONT_xCampo,
                                        "OBSCONT_xTexto": OBSCONT_xTexto,	"OBSFISCO_xCampo": OBSFISCO_xCampo,
                                        "OBSFISCO_xTexto": OBSFISCO_xTexto,	"PROCREF_nProc": PROCREF_nProc,	
                                        "PROCREF_indProc": PROCREF_indProc,	"PROCREF_tpAto": PROCREF_tpAto,
                                        })

        dados["Assinatura"].append({"Arquivo": chave,"nNF": nNF, "DigestValue": DigestValue, "SignatureValue": SignatureValue, "X509Certificate":X509Certificate})

        dados["Protocolo"].append({ "Arquivo": chave,"nNF": nNF, "tpAmb": tpAmb, "verAplic": verAplic, "chNFe": chNFe,
                                    "dhRecbto": dhRecbto, "nProt": nProt, "digVal": digVal, "cStat": cStat,	"xMotivo": xMotivo
                                   })

        return dados
#===============================================================================
    def check_none(self, var):
        return var.text if var is not None else ""

#===============================================================================
if __name__ == "__main__":
    xml = ReadXML(r'C:\Users\Igor\Desktop\XML EM UM DICIONARIO\nfe-teste')
    all_xml_files = xml.all_files()

    all_data = {}
    for file in all_xml_files:
        data_in_file = xml.nfe_data(file)
        for key, value in data_in_file.items():
            if key in all_data:
                all_data[key].extend(value)
            else:
                all_data[key] = value


    with pd.ExcelWriter(r'C:\Users\Igor\Desktop\XML EM UM DICIONARIO\DataFrame_xml\relatorio_notas_fiscais.xlsx') as writer:
        for sheet_name, data in all_data.items():
            df = pd.DataFrame(data)
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    

    print('enviado')
