
import xml.etree.ElementTree as Et
# Método principal - nfe_data    
def nfe_data(self, xml_file):
    tree = Et.parse(xml_file)
    root = tree.getroot()
    nsNfe = {"ns": "http://www.portalfiscal.inf.br/nfe"}
    nsSig = {"ns": "http://www.w3.org/2000/09/xmldsig#"}
    dados = self.initialize_data_structure()
    dados['Identificação NFE'].append(self.extract_identificacao_nfe(root, nsNfe))
    dados['Emitente'].append(self.extract_emitente_data(root, nsNfe))
    dados['Avulsa'].append(self.extract_avulsa_data(root, nsNfe))
    dados['Destinatário'].append(self.extract_destinatario_data(root, nsNfe))
    dados['Retirada'].append(self.extract_retirada_data(root, nsNfe))
    dados['Entrega'].append(self.extract_entrega_data(root, nsNfe))
    dados['Autorizadas'].append(self.extract_autorizadas_data(root, nsNfe))
    dados['Itens'] = self.extract_itens_data(root, nsNfe)
    dados['Total'].append(self.extract_total_data(root, nsNfe))
    dados['Transportadora'] = self.extract_transportadora_data(root, nsNfe)
    dados['Cobrança'] = self.extract_cobranca_data(root, nsNfe)
    dados['Pagamento'].append(self.extract_pagamento_data(root, nsNfe))
    dados['Intermediador'].append(self.extract_intermediador_data(root, nsNfe))
    dados['Inf. Adicional'].append(self.extract_inf_adicional_data(root, nsNfe))
    dados['Exportação'].append(self.extract_exportacao_data(root, nsNfe))
    dados['Compras'].append(self.extract_compras_data(root, nsNfe))
    dados['Resp. Tecnico'].append(self.extract_resp_tecnico_data(root, nsNfe))
    dados['Assinatura'].append(self.extract_assinatura_data(root, nsNfe, nsSig))
    dados['Protocolo'].append(self.extract_protocolo_data(root, nsNfe))
    return dados