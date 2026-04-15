from urllib.parse import urlencode

import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_weather(lat: float, lon: float):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current":
            "temperature_2m,"
            "is_day,"
            "weather_code,"
            "relative_humidity_2m",

        "hourly":
            "temperature_2m,"
            "precipitation_probability,"
            "weather_code,"
            "is_day",

        "daily":
            "weather_code,"
            "temperature_2m_max,"
            "temperature_2m_min,"
            "precipitation_probability_max",

        "timeformat": "unixtime",
        "forecast_days": 6, # Retourne en espace de 1 jour
        "forecast_hours": 24,
        "temporal_resolution": "hourly_3"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print(f"Erreur API: {response.status_code}")
        return None

    response.raise_for_status()
    return response.json()