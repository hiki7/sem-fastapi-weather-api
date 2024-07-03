from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = 'bd5e378503939ddaee76f12ad7a97608'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


@app.get("/weather")
def get_weather(city: str):
    response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric")

    data = response.json()

    if response.status_code != 200:
        return {"error": "City not found"}

    return {
        "city": data['name'],
        "temperature": data['main']['temp']
    }


