#   Importação de Bibliotecas
import tkinter as tk
from tkinter import filedialog

#   Quando executado, o programa solicita ao usuário a seleção da pasta dos arquivos XML.
def select_folder(title="Selecione a pasta dos arquivos XML"):
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title=title)
    return folder_path
#   Finalmente, o programa solicita ao usuário a escolha do local e nome do arquivo Excel a ser salvo.
def select_save_location(title="Selecione onde deseja salvar", file_type=[("Excel files", "*.xlsx")]):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=file_type, title=title)
    return file_path

def select_excel_file(title="Selecione um arquivo Excel"):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")], title=title)
    return file_path