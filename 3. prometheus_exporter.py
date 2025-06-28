from flask import Flask, request, jsonify, Response
import requests
import time
import psutil  # Untuk monitoring sistem
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# === METRIK PROMETHEUS ===

# Metrik untuk API model
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')  # Total request yang diterima
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP Request Latency')  # Latensi
THROUGHPUT = Counter('http_requests_throughput', 'Throughput (request per detik)')  # Throughput

# Metrik untuk monitoring sistem
CPU_USAGE = Gauge('system_cpu_usage', 'CPU Usage Percentage')  # CPU Usage
RAM_USAGE = Gauge('system_ram_usage', 'RAM Usage Percentage')  # RAM Usage

# === ENDPOINT PROMETHEUS ===
@app.route('/metrics', methods=['GET'])
def metrics():
    # Update metrik sistem saat endpoint /metrics dipanggil
    CPU_USAGE.set(psutil.cpu_percent(interval=1))
    RAM_USAGE.set(psutil.virtual_memory().percent)

    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# === ENDPOINT PREDIKSI (REVERSE PROXY) ===
@app.route('/predict', methods=['POST'])
def predict():
    start_time = time.time()
    REQUEST_COUNT.inc()
    THROUGHPUT.inc()

    data = request.get_json()
    api_url = "http://127.0.0.1:5004/invocations"  # Ganti jika port model berubah

    try:
        response = requests.post(api_url, json=data)
        latency = time.time() - start_time
        REQUEST_LATENCY.observe(latency)

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# === MAIN APP ===
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
