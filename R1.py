from flask import Flask, render_template, request, redirect

app = Flask(__name__)

stok_barang = [
    {'nama': 'Kaos Pendek', 'harga': 35000, 'stok': 10},
    {'nama': 'Kaos Panjang', 'harga': 50000, 'stok': 30},
    {'nama': 'Kaos Tidur', 'harga': 60000, 'stok': 50}
]

keranjang = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pilih = request.form.get('nama_baju')
        jumlah = int(request.form.get('jumlah') or 0)
        for baju in stok_barang:
            if pilih.lower() in baju['nama'].lower():
                if baju['stok'] >= jumlah:
                    baju['stok'] -= jumlah
                    keranjang.append({'nama': baju['nama'], 'harga': baju['harga'], 'jumlah': jumlah})
                break
        return redirect('/')
    total = sum(i['harga']*i['jumlah'] for i in keranjang)
    return render_template('index.html', stok_barang=stok_barang, keranjang=keranjang, total=total)

if __name__ == '__main__':
    from flask_cloudflared import run_with_cloudflared
    run_with_cloudflared(app)
    app.run(host='0.0.0.0', port=5000)