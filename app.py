from flask import Flask, request, render_template
import model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediksi = None
    if request.method == 'POST':
        ukuran = int(request.form['ukuran'])
        kamar = int(request.form['kamar'])
        lokasi = request.form['lokasi']
        prediksi = model.predict_price(ukuran, kamar, lokasi)
    return render_template('index.html', prediksi=prediksi)

if __name__ == '__main__':
    app.run(debug=True)