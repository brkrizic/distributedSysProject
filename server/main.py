from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from your frontend
origins = [
    "http://localhost:3000",  # Next.js frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],          # allow all HTTP methods
    allow_headers=["*"],          # allow all headers
)

# This will store received data in memory (like a temporary database)
sensor_data = []

# Define the data structure expected from sensors
class SensorReading(BaseModel):
    sensor_id: str
    temperature: float
    timestamp: str

@app.post("/sensor")
def receive_sensor(reading: SensorReading):
    sensor_data.append(reading.dict())
    print(f"Received from {reading.sensor_id}: {reading.temperature}°C at {reading.timestamp}")
    return {"status": "ok"}
    
@app.get("/data")
def get_all_data():
    return sensor_data
