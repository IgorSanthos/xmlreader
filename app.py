from flask  import Flask, render_template, redirect, url_for
from main import xmltoExcel
from out_xml import exceltoXml

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')


@app.route('/xml', methods=['POST'])
def xmlTo():
    select_folder = r'C:/Users/Igor/Desktop/143'
    select_save_location = r'C:/Users/Igor/Desktop/143/arquivo_xml_to_excel.xlsx'
    xmltoExcel(select_folder,select_save_location)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
