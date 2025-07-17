
# Sleep Health Prediction System: XGBoost Model

**Deskripsi Proyek:**

Proyek ini bertujuan untuk memprediksi gangguan tidur berdasarkan data gaya hidup menggunakan model XGBoost. Model ini dilatih menggunakan data kesehatan tidur, dan dilengkapi dengan Continuous Integration (CI) menggunakan GitHub Actions untuk otomatisasi pengujian, pembangunan, dan deployment model. Selain itu, sistem ini juga mencakup pemantauan kinerja dan logging model menggunakan Prometheus dan Grafana untuk memastikan performa model tetap optimal di lingkungan produksi.



## Fitur Utama

* **Model XGBoost:** Menggunakan XGBoost untuk membangun model prediksi gangguan tidur.
* **CI/CD dengan GitHub Actions:** CI digunakan untuk otomatisasi pengujian dan deployment.
* **MLflow:** Digunakan untuk mengelola siklus hidup model, mulai dari pelatihan hingga deployment.
* **Prometheus & Grafana:** Digunakan untuk pemantauan dan visualisasi performa model dalam lingkungan produksi.



## Struktur Proyek

```
monitoring-logging/
├── 1. bukti_serving/
│   ├── bukti_serving-docker.png
│   ├── bukti_serving-inference.png
│   └── bukti_serving-mlflow.png
├── 4. bukti monitoring Prometheus/
│   ├── monitoring_http_requests_duration_seconds.png
│   ├── monitoring_http_request_total.png
│   ├── monitoring_system_cpu_usage.png
│   └── monitoring_sytem_ram_usage.png
├── 5. bukti monitoring Grafana/
│   ├── dashboard_grafana-1.png
│   ├── dashboard_grafana-2.png
│   ├── dashboard_grafana-3.png
│   ├── monitoring_distribusi_waktu_permintaan.png
│   ├── monitoring_Jumlah_Python_GC_dijalankan_per_Collection.png
│   ├── monitoring_jumlah_request_API.png
│   ├── monitoring_objek_dikumpulkan.png
│   ├── monitoring_penambahan_series_scrape.png
│   ├── monitoring_penggunaan_CPU.png
│   ├── monitoring_penggunaan_RAM.png
│   ├── monitoring_relabel_impact_tracker.png
│   ├── monitoring_scrape_duration.png
│   └── monitoring_total_waktu_permintaan.png
├── 6. bukti alerting Grafana/
│   ├── alert_CPU_tinggi.png
│   ├── alert_latensi_HTTP_tinggi.png
│   ├── alert_RAM_hampir_penuh.png
│   ├── rules_CPU_tinggi.png
│   ├── rules_latensi_HTTP_tinggi.png
│   └── rules_RAM_hampir_penuh.png
├── .gitignore
├── 2. prometheus.yml
├── 3. prometheus_exporter.py
├── 7. inference.py
├── modelling.py
├── requirements.txt
├── sleep-health_life-style_preprocessing.csv
└── xgboost_best_model.joblib
```


## Requirements

1. Python 3.9.2
2. XGBoost
3. MLflow
4. Prometheus
5. Grafana
6. Docker 



## Setup dan Instalasi

### 1. Clone repositori ini ke mesin lokal :
```bash
git clone https://github.com/labibaadinda/Workflow-CI
```

### 2. Buat dan aktifkan environment menggunakan Conda:

```bash
conda env create -f MLProject/conda.yaml
conda activate mlflow-env
```

### 3. Install dependensi yang diperlukan:

```bash
cd MLProject
pip install -r requirements.txt
```



## Membuat Serving Model

Untuk melakukan serving model di lingkungan lokal, dapat menggunakan **MLflow model serve**. Pastikan MLflow sudah terinstall dan jalankan perintah berikut untuk mengaktifkan model untuk inference:

```bash
mlflow models serve -m "file://$(pwd)/xgboost_model_dir" --host 0.0.0.0 --port 5001
```

Menggunakan Docker untuk deployment, bisa membangun dan menjalankan Docker container seperti berikut:

```bash
docker build -t xgb_model_image .
docker run -p 5001:5001 xgb_model_image
```

### Bukti Serving Model

* Bukti hasil serving model dapat ditemukan pada folder `bukti_serving`. 



## Monitoring Menggunakan Prometheus

Proyek ini menggunakan **Prometheus** untuk memonitoring performa model secara real-time. Anda dapat mengonfigurasi **Prometheus exporter** yang akan melacak metrik yang relevan dari model yang di-serve.

### 1. File Konfigurasi Prometheus

File konfigurasi Prometheus `prometheus.yml` digunakan untuk menentukan sumber data dan metriks yang akan dipantau.

### 2. Prometheus Exporter

Untuk mengumpulkan metrik dari model yang di-serve, dapat menggunakan `prometheus_exporter.py`, yang berfungsi untuk mengekspor metrik dari API model.

### Bukti Monitoring Prometheus

* Hasil tangkapan layar monitoring Prometheus dapat ditemukan di dalam folder `bukti monitoring Prometheus`. Pastikan untuk menangkap berbagai metrik yang relevan dengan performa model, seperti latensi dan throughput.



## Visualisasi dengan Grafana

Setelah Prometheus berhasil mengumpulkan metrik, kita dapat menggunakan **Grafana** untuk visualisasi data dan memonitor performa model.

### 1. Setup Grafana

1. Unduh dan jalankan Grafana di mesin lokal atau server.
2. Konfigurasikan Grafana untuk terhubung dengan Prometheus sebagai sumber data.
3. Buat **Dashboard** di Grafana untuk memonitor metrik performa model.

### Bukti Monitoring Grafana

* Hasil visualisasi metrik dalam Grafana dapat ditemukan di dalam folder `bukti monitoring Grafana`. Pastikan tangkapan layar mencakup berbagai metrik yang dipantau (minimal 5 metrik berbeda).



## Alerting dengan Grafana

Selain monitoring, juga dapat mengonfigurasi **alerting** di Grafana untuk memberi notifikasi apabila metrik model melebihi ambang batas tertentu.

### Konfigurasi Alerting Grafana

1. Di dashboard Grafana, tentukan aturan alerting berdasarkan metrik tertentu (misalnya, latensi atau tingkat kesalahan).
2. Setel notifikasi yang akan dikirim via email atau webhook ketika alert dipicu.

### Bukti Alerting Grafana

* Hasil tangkapan layar alerting Grafana dapat ditemukan di dalam folder `bukti alerting Grafana`. Pastikan untuk menunjukkan rules dan notifikasi yang dihasilkan oleh Grafana.



## Inference Model

Untuk melakukan inference pada model yang telah diserve,  dapat menggunakan script `inference.py`. 

## Catatan

* **Prometheus** digunakan untuk mengumpulkan metrik performa dari model yang di-serve.
* **Grafana** digunakan untuk visualisasi metrik dan pembuatan alerting untuk memonitor model dalam produksi.

