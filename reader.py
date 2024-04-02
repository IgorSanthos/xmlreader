#                           FUNCOES IMPORTANTES 
#                           IMPRIMIR O XML COMPLETO print(ET.dump(root))

import xml.etree.ElementTree as ET
# Definindo o namespace padrão



try:

#   Acessar o arquivo xml 
    tree = ET.parse('427.xml')

# Acessa a primeira Raiz, o nome da raiz esta dentro da TAG <nfeProc> no caso é o http://www.portalfiscal.inf.br/nfe
    root = tree.getroot()

    # Remover namespace dos elementos usando expressões XPath
    for elem in root.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]  # Remove o namespace do nome da tag

# Criando variavel para a TAG desejada no caso CFOP deve-se colocar o caminho sempre que quer ir atras de alguma TAG(.//nfe: )
    element_CFOP = './/CFOP'
    element_nNF = './/nNF'


#   Criando variavel para a tag que quero encontrar
    cFOP = root.find(element_CFOP)
    nNF = root.find(element_nNF)

                                #   variavel da mudança do valor da TAG
                                    #element_change = '5949'

                                #   Recebimento da TAG original para a Mudança
                                    #og_element.text = element_change
    
                                #   Exportar o XML modificado
    


#   Validador de TAG
    if  cFOP is not None:
        cFOP_content = cFOP.text
        nNF_content = nNF.text
        tree.write(f'{nNF_content}_modified.xml',xml_declaration=True, encoding='utf-8', method='xml',short_empty_elements=False)
        print("Conteúdo da TAG:", cFOP_content)
    else:
        print("Elemento CFOP não encontrado.")
    



































except Exception as error:
    print("*****************************************************************", error,"*****************")