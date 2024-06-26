import pandas as pd
import xml.etree.ElementTree as ET
# Essa função, `df_to_xml`, converte um DataFrame do pandas em elementos XML, organizando-os hierarquicamente conforme as especificações fornecidas por tags de primeiro, segundo e terceiro níveis e evitando colunas especificadas para pular.
def df_to_xml(df, parent_element, row_element_name, tag_first_lvl=None, tag_sec_lvl=None, tag_ter_lvl=None, skip_columns=None):
    for _, row in df.iterrows():
        # Verifica se todas as colunas a partir da terceira estão vazias
        all_empty = all(pd.isna(row[col_name]) or row[col_name] in ['', ' '] for col_name in df.columns[2:])
        if all_empty:
            continue
        
        row_element = ET.SubElement(parent_element, row_element_name)
        for col_name in df.columns:
            if pd.isna(row[col_name]) or row[col_name] in ['', ' ']:
                continue
            if skip_columns and col_name in skip_columns:
                continue
            if tag_first_lvl and col_name in tag_first_lvl:
                sub_element_name = tag_first_lvl[col_name]
                sub_element = row_element.find(sub_element_name) or ET.SubElement(row_element, sub_element_name)
                if tag_sec_lvl and col_name in tag_sec_lvl:
                    sub_sub_element_name = tag_sec_lvl[col_name]
                    sub_sub_element = sub_element.find(sub_sub_element_name) or ET.SubElement(sub_element, sub_sub_element_name)
                    if tag_ter_lvl and col_name in tag_ter_lvl:
                        sub_sub_sub_element_name = tag_ter_lvl[col_name]
                        sub_sub_sub_element = sub_sub_element.find(sub_sub_sub_element_name) or ET.SubElement(sub_sub_element, sub_sub_sub_element_name)
                        cell = ET.SubElement(sub_sub_sub_element, col_name)
                    else:
                        cell = ET.SubElement(sub_sub_element, col_name)
                else:
                    cell = ET.SubElement(sub_element, col_name)
                cell.text = str(row[col_name])
            else:
                cell = ET.SubElement(row_element, col_name)
                cell.text = str(row[col_name])