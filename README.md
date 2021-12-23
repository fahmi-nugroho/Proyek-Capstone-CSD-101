<p align="center">
  <img height="100" src="https://github.com/fahmi-nugroho/Proyek-Capstone-CSD-101/blob/0be44b291e3eb6f7f984e0db54996493322438b6/static/img/logo.png">
</p>

# DIABECHECK! - Aplikasi Prediksi Risiko Diabetes Tahap Awal

## Latar Belakang Aplikasi
Diabetes adalah penyakit kronis yang menyebabkan peningkatan gula darah, dan menjadi salah satu penyakit yang mematikan di dunia. Ditambah situasi Covid-19 sekarang ini, menyebabkan sebagian besar masyarakat enggan untuk memeriksakan diri ke pusat kesehatan karena prosedur tambahan yang diterapkan. Adanya pandemi Covid-19 membuat orang dengan diabetes beresiko lebih besar jika dibandingkan orang yang sehat. Dari permasalah tersebut, kami memutuskan membuat aplikasi prediksi risiko diabetes tahap awal, untuk membantu proses diagnosa awal agar pada pengguna dapat mencegah resiko sedini mungkin. Kami menamainya dengan ‘Diabecheck!’ yaitu kepanjangan dari ‘Diabetes Check!’.

## Cara Menjalankan di Lokal
1. Clone repository ini
```
  git clone https://github.com/fahmi-nugroho/Proyek-Capstone-CSD-101.git
```
2. Install Virtual Environemnt
```
  virtualenv env
```
3. Install Requirements
```
  pip install -r requirements.txt
```
4. Import Flask App & Run
```
  export FLASK_APP=app.py
  flask run
```

## Cara Mengakses Website
Silahkan kunjungi situs berikut [Diabecheck!](https://diabecheck.herokuapp.com/)

## Fitur-Fitur Pada Aplikasi
- [x] Terdapat kuisioner untuk mendiagnosa keadaan pengguna
- [x] Menampilkan hasil diagnosa pada pengguna

## Sumber Daya Aplikasi
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Heroku](https://www.heroku.com/home)
- [Image](https://unsplash.com/)

## Dataset yang Digunakan
- [Early Stage Diabetes Risk Prediction Dataset](https://www.kaggle.com/ishandutta/early-stage-diabetes-risk-prediction-dataset)

## Artikel
- [Prediksi Kemungkinan Diabetes pada Tahap Awal Menggunakan Algoritma Klasifikasi Random Forest](https://www.researchgate.net/publication/349480328_Prediksi_Kemungkinan_Diabetes_pada_Tahap_Awal_Menggunakan_Algoritma_Klasifikasi_Random_Forest)
- [Sistem Prediksi Penyakit Diabetes Berbasis Decision Tree](https://ejournal.bsi.ac.id/ejurnal/index.php/Bianglala/article/view/554)
- [Analisis Faktor Risiko Kematian dengan Penyakit Komorbid Covid-19](https://journal.ipm2kpe.or.id/index.php/JKS/article/view/1587)

## Tim Pengembang
- [Fahmi Nugroho Alibasyah](https://github.com/fahmi-nugroho)
- [Ni Putu Sintia Wati](https://github.com/sintiasnn)
