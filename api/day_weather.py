import requests

from utilitaire.conversion import Conversion
from utilitaire.get_weather_icon import weather_icon

class DayWeather:

    def get_day_weather(self, lat, lon):
        url_weather = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
                       f"&hourly="
                       f"temperature_2m,"
                       f"precipitation_probability,"
                       f"weather_code,"
                       f"is_day"
                       f"&forecast_days=1"
                       f"&timeformat=unixtime"
                       f"&forecast_hours=24&"
                       f"temporal_resolution=hourly_3")
        response = requests.get(url_weather)
        if response.status_code == 200:
            data = response.json()
            weather = [weather_icon.get_weather_icon(weather_code, is_day)
                        for weather_code, is_day in zip(data["hourly"]["weather_code"], data["hourly"]["is_day"])]
            return {
                "temperature_2m": [round(temp) for temp in data["hourly"]["temperature_2m"]],
                "icon": [w["icon"] for w in weather],
                "preci_proba": [preci for preci in data["hourly"]["precipitation_probability"]],
                "time": [Conversion.from_timestamp_to_hour(time) for time in data["hourly"]["time"]]
            }
        elif response.status_code == 400:
            data = response.json()
            print(data["error"] + " : " + data["reason"])
            return None
        else:
            print("Erreur lors de la requête : " + str(response.status_code))
            return None