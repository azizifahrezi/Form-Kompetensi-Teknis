from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Baca file Excel baru
data = pd.read_excel('data_kompetensi_v2.xlsx')

# Ambil daftar unik Job Function
job_functions = sorted(data['Job Function'].dropna().unique())

@app.route('/')
def index():
    return render_template('index.html', job_functions=job_functions)

@app.route('/get_kompetensi', methods=['GET'])
def get_kompetensi():
    job_function = request.args.get('job_function')
    if not job_function:
        return jsonify([])

    # Filter data berdasarkan Job Function
    kompetensi_list = sorted(data[data['Job Function'] == job_function]['Kompetensi Teknis'].dropna().unique())
    return jsonify(kompetensi_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
