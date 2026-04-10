import requests
from utilitaire.get_weather_icon import weather_icon

class CurrentWeather:

    def get_current_weather(self, lat, lon):
        url_weather = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
                       f"&current="
                       f"temperature_2m,"
                       f"is_day,"
                       f"weather_code,"
                       f"relative_humidity_2m"
                       f"&timeformat=unixtime")
        response = requests.get(url_weather)
        if response.status_code == 200:
            data = response.json()
            weather = weather_icon.get_weather_icon(self, data["current"]["weather_code"], data["current"]["is_day"])
            return {
                "temperature_2m": round(data["current"]["temperature_2m"]),
                "icon": weather["icon"],
                "description": weather["description"],
                "humidity": data["current"]["relative_humidity_2m"],
                "time": data["current"]["time"]
            }
        elif response.status_code == 400:
            data = response.json()
            print(data["error"] + " : " + data["reason"])
            return None
        else:
            print("Erreur lors de la requête : " + str(response.status_code))
            return None