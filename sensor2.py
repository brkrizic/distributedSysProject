import requests
import time
import random
from datetime import datetime

URL = "http://127.0.0.1:8000/sensor"

try:
    while True:
        temp = round(random.uniform(25.0, 35.0), 2)
        reading = {
            "sensor_id": "sensor2",
            "temperature": temp,
            "timestamp": str(datetime.now())
        }
        response = requests.post(URL, json=reading)
        print(f"Sent: {reading} | Response: {response.json()}")
        time.sleep(30)
except KeyboardInterrupt:
    print("Sensor2 stopped.")
