import pandas as pd
import xml.etree.ElementTree as ET
import glob
import os

# Função para converter DataFrame para XML e adicionar ao root existente
def dataframe_to_xml(df, root, row_element_name, sub_element_mapping=None):
    for _, row in df.iterrows():
        row_element = ET.SubElement(root, row_element_name)
        
        for col_name in df.columns:
            if sub_element_mapping and col_name in sub_element_mapping:
                sub_element_name = sub_element_mapping[col_name]
                sub_element = row_element.find(sub_element_name)
                if sub_element is None:
                    sub_element = ET.SubElement(row_element, sub_element_name)
                cell = ET.SubElement(sub_element, col_name)
            else:
                cell = ET.SubElement(row_element, col_name)
            cell.text = str(row[col_name])
#=================================================================


# Diretório contendo o arquivo Excel
excel_files = glob.glob(r'C:\Users\Igor\Desktop\XML EM UM DICIONARIO\DataFrame_xml/*.xlsx')
excel_file = excel_files[0]
#=================================================================

# Ler os dados das duas planilhas
df_sheet1 = pd.read_excel(excel_file, sheet_name="Identificação NFE")
df_sheet2 = pd.read_excel(excel_file, sheet_name="Emitente")
#==================================================================

# Mapeamento de sub-elementos para a aba "Sheet2"
sub_element_mapping_sheet2 = {
    "xLgr": "enderEmit",
    "nro": "enderEmit",
    "xCpl": "enderEmit",
    "xBairro": "enderEmit",
    "cMun": "enderEmit",
    "xMun": "enderEmit",
    "UF": "enderEmit",
    "CEP": "enderEmit",
    "cPais": "enderEmit",
    "xPais": "enderEmit",
    "fone": "enderEmit"
}
#======================================================

# Identificar valores únicos na coluna "chave"
chaves_unicas = df_sheet1['Arquivo'].unique()

# Criar uma pasta para salvar os arquivos XML
output_directory = r'C:\Users\Igor\Desktop\XML EM UM DICIONARIO\DataFrame_xml\XML_Output'
os.makedirs(output_directory, exist_ok=True)
#==================================================================

# Processar cada valor único na coluna "chave"
for chave in chaves_unicas:
    # Filtrar as linhas correspondentes à chave atual
    df_sheet1_chave = df_sheet1[df_sheet1['Arquivo'] == chave]
    df_sheet2_chave = df_sheet2[df_sheet2['Arquivo'] == chave]
    
    # Inicializar o elemento root
    root_element_name = 'nfeProc'
    root = ET.Element(root_element_name)
#===================================================================
    
    # Adicionar dados da Sheet1
    dataframe_to_xml(df_sheet1_chave, root, 'ide')    
    # Adicionar dados da Sheet2
    dataframe_to_xml(df_sheet2_chave, root, 'emit', sub_element_mapping=sub_element_mapping_sheet2)
#=====================================================================    

    # Converter o elemento root para string XML
    xml_data = ET.tostring(root, encoding='unicode')
    
    # Caminho para o arquivo XML de saída
    output_xml_file = os.path.join(output_directory, f'NFE_{chave}.xml')
    with open(output_xml_file, 'w', encoding='utf-8') as f:
        f.write(xml_data)

    print(f'Arquivo XML para chave {chave} salvo em {output_xml_file}')
