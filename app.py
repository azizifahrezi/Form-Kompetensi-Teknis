from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Nama file excel
EXCEL_FILE = "Daftar Kompetensi Teknis.xlsx"

def load_kompetensi():
    """Membaca data dari Excel dan mengembalikan list kompetensi"""
    df = pd.read_excel(EXCEL_FILE, engine='openpyxl')
    kompetensi = df['Kompetensi_Teknis'].dropna().tolist()
    return kompetensi

@app.route('/')
def index():
    kompetensi_list = load_kompetensi()
    level_list = [1, 2, 3, 4, 5]  # Level tetap
    return render_template('index.html', kompetensi_list=kompetensi_list, level_list=level_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
