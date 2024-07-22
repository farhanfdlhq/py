from flask import Flask, jsonify
from flask_cors import CORS
import json
from collections import Counter

app = Flask(__name__)
CORS(app)

def load_pariwisata_data():
    with open('pariwisata.json') as f:
        return json.load(f)

@app.route('/api/pariwisata', methods=['GET'])
def get_pariwisata_data():
    data = load_pariwisata_data()
    return jsonify(data)

@app.route('/api/pariwisata/jenis_usaha', methods=['GET'])
def get_jenis_usaha_data():
    data = load_pariwisata_data()
    jenis_usaha_counts = Counter(item['jenis_usaha'] for item in data)
    return jsonify(jenis_usaha_counts)

@app.route('/api/pariwisata/kecamatan', methods=['GET'])
def get_kecamatan_data():
    data = load_pariwisata_data()
    kecamatan_counts = Counter(item['kecamatan'] for item in data)
    return jsonify(kecamatan_counts)

@app.route('/api/pariwisata/wilayah', methods=['GET'])
def get_wilayah_data():
    data = load_pariwisata_data()
    wilayah_counts = Counter(item['wilayah'] for item in data)
    return jsonify(wilayah_counts)

@app.route('/api/pariwisata/sebaran_jenis_usaha_per_kecamatan', methods=['GET'])
def get_sebaran_jenis_usaha_per_kecamatan_data():
    data = load_pariwisata_data()
    sebaran_jenis_per_kecamatan = {}
    
    for item in data:
        kecamatan = item['kecamatan']
        jenis_usaha = item['jenis_usaha']
        if kecamatan not in sebaran_jenis_per_kecamatan:
            sebaran_jenis_per_kecamatan[kecamatan] = []
        sebaran_jenis_per_kecamatan[kecamatan].append(jenis_usaha)
    
    result = {kecamatan: len(set(jenis_usaha)) for kecamatan, jenis_usaha in sebaran_jenis_per_kecamatan.items()}
    return jsonify(result)

@app.route('/api/pariwisata/sebaran_kecamatan_per_wilayah', methods=['GET'])
def get_sebaran_kecamatan_per_wilayah_data():
    data = load_pariwisata_data()
    sebaran_kecamatan_per_wilayah = {}
    
    for item in data:
        wilayah = item['wilayah']
        kecamatan = item['kecamatan']
        if wilayah not in sebaran_kecamatan_per_wilayah:
            sebaran_kecamatan_per_wilayah[wilayah] = []
        sebaran_kecamatan_per_wilayah[wilayah].append(kecamatan)
    
    result = {wilayah: len(set(kecamatan)) for wilayah, kecamatan in sebaran_kecamatan_per_wilayah.items()}
    return jsonify(result)

@app.route('/api/pariwisata/sebaran_jenis_usaha_per_wilayah', methods=['GET'])
def get_sebaran_jenis_usaha_per_wilayah_data():
    data = load_pariwisata_data()
    sebaran_jenis_per_wilayah = {}
    
    for item in data:
        wilayah = item['wilayah']
        jenis_usaha = item['jenis_usaha']
        if wilayah not in sebaran_jenis_per_wilayah:
            sebaran_jenis_per_wilayah[wilayah] = []
        sebaran_jenis_per_wilayah[wilayah].append(jenis_usaha)
    
    result = {wilayah: len(set(jenis_usaha)) for wilayah, jenis_usaha in sebaran_jenis_per_wilayah.items()}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
