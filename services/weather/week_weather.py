import requests

from utilitaire.conversion import Conversion
from utilitaire.get_weather_icon import weather_icon

class WeekWeather:

    def get_week_weather(self, lat, lon):
        url_weather = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
                       f"&daily="
                       f"weather_code,"
                       f"temperature_2m_max,"
                       f"temperature_2m_min,"
                       f"precipitation_probability_max&"
                       f"timeformat=unixtime")
        print(url_weather)
        response = requests.get(url_weather)
        if response.status_code == 200:
            data = response.json()
            weather = [weather_icon.get_weather_icon(weather_code, 1)
                       for weather_code in data["daily"]["weather_code"]]
            return {
                "temperature_min": [round(temp) for temp in data["daily"]["temperature_2m_min"]],
                "temperature_max": [round(temp) for temp in data["daily"]["temperature_2m_max"]],
                "icon": [w["icon"] for w in weather],
                "preci_proba": [preci for preci in data["daily"]["precipitation_probability_max"]],
                "time": [Conversion.from_timestamp_to_day(time) for time in data["daily"]["time"]]
            }
        elif response.status_code == 400:
            data = response.json()
            print(data["error"] + " : " + data["reason"])
            return None
        else:
            print("Erreur lors de la requête : " + str(response.status_code))
            return None