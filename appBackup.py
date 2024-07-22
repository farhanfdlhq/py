from flask import Flask, jsonify, send_file
import json
import matplotlib.pyplot as plt
import io
import base64
from collections import Counter

app = Flask(__name__)

def load_pariwisata_data():
    with open('pariwisata.json') as f:
        return json.load(f)

@app.route('/api/pariwisata', methods=['GET'])
def get_pariwisata_data():
    data = load_pariwisata_data()
    return jsonify(data)

@app.route('/api/pariwisata/jenis_usaha', methods=['GET'])
def get_jenis_usaha_chart():
    data = load_pariwisata_data()
    jenis_usaha_counts = Counter(item['jenis_usaha'] for item in data)
    
    plt.figure(figsize=(10, 6))
    plt.bar(jenis_usaha_counts.keys(), jenis_usaha_counts.values())
    plt.title('Jumlah Jenis Usaha di Jakarta')
    plt.xlabel('Jenis Usaha')
    plt.ylabel('Jumlah')
    plt.xticks(rotation=45)
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/api/pariwisata/kecamatan', methods=['GET'])
def get_kecamatan_chart():
    data = load_pariwisata_data()
    kecamatan_counts = Counter(item['kecamatan'] for item in data)
    
    plt.figure(figsize=(10, 6))
    plt.bar(kecamatan_counts.keys(), kecamatan_counts.values())
    plt.title('Jumlah Kecamatan dengan Jenis Usaha di Jakarta')
    plt.xlabel('Kecamatan')
    plt.ylabel('Jumlah')
    plt.xticks(rotation=45)
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/api/pariwisata/wilayah', methods=['GET'])
def get_wilayah_chart():
    data = load_pariwisata_data()
    wilayah_counts = Counter(item['wilayah'] for item in data)
    
    plt.figure(figsize=(10, 6))
    plt.bar(wilayah_counts.keys(), wilayah_counts.values())
    plt.title('Jumlah Wilayah dengan Jenis Usaha di Jakarta')
    plt.xlabel('Wilayah')
    plt.ylabel('Jumlah')
    plt.xticks(rotation=45)
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/api/pariwisata/sebaran_jenis_usaha_per_kecamatan', methods=['GET'])
def get_sebaran_jenis_usaha_per_kecamatan_chart():
    data = load_pariwisata_data()
    sebaran_jenis_per_kecamatan = {}
    
    for item in data:
        kecamatan = item['kecamatan']
        jenis_usaha = item['jenis_usaha']
        if kecamatan not in sebaran_jenis_per_kecamatan:
            sebaran_jenis_per_kecamatan[kecamatan] = []
        sebaran_jenis_per_kecamatan[kecamatan].append(jenis_usaha)
    
    kecamatan_keys = list(sebaran_jenis_per_kecamatan.keys())
    jenis_counts_per_kecamatan = [len(set(sebaran_jenis_per_kecamatan[kec])) for kec in kecamatan_keys]
    
    plt.figure(figsize=(10, 6))
    plt.bar(kecamatan_keys, jenis_counts_per_kecamatan)
    plt.title('Sebaran Jenis Usaha di Setiap Kecamatan')
    plt.xlabel('Kecamatan')
    plt.ylabel('Jumlah Jenis Usaha')
    plt.xticks(rotation=45)
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/api/pariwisata/sebaran_kecamatan_per_wilayah', methods=['GET'])
def get_sebaran_kecamatan_per_wilayah_chart():
    data = load_pariwisata_data()
    sebaran_kecamatan_per_wilayah = {}
    
    for item in data:
        wilayah = item['wilayah']
        kecamatan = item['kecamatan']
        if wilayah not in sebaran_kecamatan_per_wilayah:
            sebaran_kecamatan_per_wilayah[wilayah] = []
        sebaran_kecamatan_per_wilayah[wilayah].append(kecamatan)
    
    wilayah_keys = list(sebaran_kecamatan_per_wilayah.keys())
    kecamatan_counts_per_wilayah = [len(set(sebaran_kecamatan_per_wilayah[wil])) for wil in wilayah_keys]
    
    plt.figure(figsize=(10, 6))
    plt.bar(wilayah_keys, kecamatan_counts_per_wilayah)
    plt.title('Sebaran Kecamatan dengan Jenis Usaha di Setiap Wilayah')
    plt.xlabel('Wilayah')
    plt.ylabel('Jumlah Kecamatan')
    plt.xticks(rotation=45)
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/api/pariwisata/sebaran_jenis_usaha_per_wilayah', methods=['GET'])
def get_sebaran_jenis_usaha_per_wilayah_chart():
    data = load_pariwisata_data()
    sebaran_jenis_per_wilayah = {}
    
    for item in data:
        wilayah = item['wilayah']
        jenis_usaha = item['jenis_usaha']
        if wilayah not in sebaran_jenis_per_wilayah:
            sebaran_jenis_per_wilayah[wilayah] = []
        sebaran_jenis_per_wilayah[wilayah].append(jenis_usaha)
    
    wilayah_keys = list(sebaran_jenis_per_wilayah.keys())
    jenis_counts_per_wilayah = [len(set(sebaran_jenis_per_wilayah[wil])) for wil in wilayah_keys]
    
    plt.figure(figsize=(10, 6))
    plt.bar(wilayah_keys, jenis_counts_per_wilayah)
    plt.title('Sebaran Jenis Usaha di Setiap Wilayah')
    plt.xlabel('Wilayah')
    plt.ylabel('Jumlah Jenis Usaha')
    plt.xticks(rotation=45)
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
