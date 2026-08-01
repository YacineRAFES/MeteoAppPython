import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_weather_for_list_cities(villes_data: list):
    """
    Récupère la météo de la liste des villes en une seule requête

    Parameters
        villes_data: liste de dictionnaires contenant la liste des villes
        - latitude
        - longitude

    Returns
        Données météo pour toutes les villes
    """
    lat = [ville["latitude"] for ville in villes_data]
    lon = [ville["longitude"] for ville in villes_data]

    params = {
        "latitude": ",".join(map(str, lat)),
        "longitude": ",".join(map(str, lon)),
        "current":
            "temperature_2m,"
            "is_day,"
            "weather_code,"
            "relative_humidity_2m",

        "timeformat": "unixtime"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print(f"Erreur API: {response.status_code}")
        return None

    response.raise_for_status()
    data = response.json()

    if isinstance(data, dict):
        data = [data]

    return data

def fetch_weather(lat: float, lon: float, models: list):
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
            "is_day,"
            "precipitation",

        "daily":
            "weather_code,"
            "temperature_2m_max,"
            "temperature_2m_min,"
            "precipitation_probability_max",

        "timeformat": "unixtime",
        "forecast_days": 6,
        "forecast_hours": 24,
        "temporal_resolution": "hourly_1",
        "models": models
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print(f"Erreur API: {response.status_code}")
        return None

    response.raise_for_status()
    return response.json()