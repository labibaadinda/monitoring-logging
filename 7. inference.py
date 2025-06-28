import requests

# Endpoint monitoring Flask
url = "http://127.0.0.1:8000/predict"
headers = {"Content-Type": "application/json"}

# Data input
payload = {
    "dataframe_split": {
        "columns": [
            "Person ID", "Gender", "Age", "Occupation", "Sleep Duration",
            "Quality of Sleep", "Physical Activity Level", "Stress Level",
            "BMI Category", "Heart Rate", "Daily Steps", "Systolic BP", "Diastolic BP"
        ],
        "data": [
            [400, 1, 28, 2, 5, 6, 40, 6, 0, 72, 6000, 120, 80]
        ]
    }
}

# Kirim permintaan prediksi ke monitoring API
response = requests.post(url, json=payload, headers=headers)

# Mapping label hasil prediksi
pred_label_map = {
    0: "Normal",
    1: "Insomnia",
    2: "Sleep Apnea"
}

# Tampilkan hasil
try:
    prediction = response.json()["predictions"][0]
    label = pred_label_map.get(prediction, "Unknown")
    print(f"Prediction result: {label}")
except Exception as e:
    print("Error reading prediction:", e)
    print("Raw response:", response.text)
