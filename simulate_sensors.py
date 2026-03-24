import requests
import random
import time
import json
from datetime import datetime

API_URL = "http://localhost:8000/upload-data"
DEVICE_ID = "NODE_01"

def generate_reading():
    # Simulate realistic sensor data
    # AQI: 0-500 (Good to Hazardous)
    # Temp: 20-40 C
    # Humidity: 30-90 %
    # Noise: 40-100 dB
    # pH: 0-14
    # Turbidity: 0-100 NTU
    
    return {
        "device_id": DEVICE_ID,
        "aqi": round(random.uniform(20, 180), 2),  # Mix of good and bad
        "temperature": round(random.uniform(25, 35), 1),
        "humidity": round(random.uniform(40, 80), 1),
        "noise_db": round(random.uniform(45, 95), 1), # Occasional high noise
        "ph": round(random.uniform(6.0, 8.0), 2),
        "turbidity": round(random.uniform(5, 50), 2)
    }

def main():
    print(f"Starting sensor simulation for device {DEVICE_ID}...")
    print(f"Target: {API_URL}")
    
    while True:
        try:
            data = generate_reading()
            response = requests.post(API_URL, json=data)
            
            if response.status_code == 200:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Data sent: AQI={data['aqi']}, Noise={data['noise_db']}dB")
            else:
                print(f"Error sending data: {response.status_code} - {response.text}")
                
        except Exception as e:
            print(f"Connection error: {e}")
            print("Is the backend server running?")
            
        time.sleep(5)

if __name__ == "__main__":
    main()
