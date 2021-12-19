from flask import Flask, render_template, request
from preprocess import reshape
import joblib

app = Flask(__name__)
model = joblib.load('models/randomforest_model.pkl')

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/sub", methods = ['POST'])
def submit():
    if request.method == "POST":
        nama = request.form.get("nama")
        umur = request.form.get("umur")
        jenisKelamin = request.form['jenis_kelamin']
        polyuria = 1 if request.form.get("polyuria") == "1" else 0
        polydipsia = 1 if request.form.get("polydipsia") == "1" else 0
        penurunanBB = 1 if request.form.get("penurunanBB") == "1" else 0
        lemas = 1 if request.form.get("lemas") == "1" else 0
        nafsuMakan = 1 if request.form.get("nafsuMakan") == "1" else 0
        infeksiKelamin = 1 if request.form.get("infeksiKelamin") == "1" else 0
        pandangan = 1 if request.form.get("pandangan") == "1" else 0
        gatal = 1 if request.form.get("gatal") == "1" else 0
        mood = 1 if request.form.get("mood") == "1" else 0
        penyembuhan = 1 if request.form.get("penyembuhan") == "1" else 0
        gerakanBadan = 1 if request.form.get("gerakanBadan") == "1" else 0
        otot = 1 if request.form.get("otot") == "1" else 0
        rambut = 1 if request.form.get("rambut") == "1" else 0
        obesitas = 1 if request.form.get("obesitas") == "1" else 0
    
    data = reshape(
        umur,
        jenisKelamin,
        polyuria,
        polydipsia,
        penurunanBB,
        lemas,
        nafsuMakan,
        infeksiKelamin,
        pandangan,
        gatal,
        mood,
        penyembuhan,
        gerakanBadan,
        otot,
        rambut,
        obesitas
    )

    hasil = model.predict_proba(data)
    
    prediksi = "Positif" if hasil[0][0] <= hasil[0][1] else "Negative"

    if prediksi == "Positif":
        persentase = hasil[0][1] * 100
        data = [nama, persentase]
        return render_template("result-pos.html", d = data)
    else:
        persentase = hasil[0][0] * 100
        data = [nama, persentase]
        return render_template("result-neg.html", d = data)

if __name__ == "__main__":
    app.run(debug=True)