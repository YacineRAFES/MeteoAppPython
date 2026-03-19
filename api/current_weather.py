import requests
from utilitaire.get_weather_icon import weather_icon
from api.geocoding import GeoCoding

class current_weather:

    def get_current_weather(self, nomville):
        geo = GeoCoding.GetGeo(self, nomville)
        url_weather = f"https://api.open-meteo.com/v1/forecast?latitude={geo['latitude']}&longitude={geo['longitude']}&current=temperature_2m,is_day,weather_code&timeformat=unixtime"
        response = requests.get(url_weather)
        if response.status_code == 200:
            data = response.json()
            weather = weather_icon.get_weather_icon(self, data["current"]["weather_code"], data["current"]["is_day"])
            return {
                "temperature_2m": round(data["current"]["temperature_2m"]),
                "icon": weather["icon"],
                "description": weather["description"],
                "code_country": geo["code_country"]
            }
        elif response.status_code == 400:
            data = response.json()
            return {
                print(data["error"] + " : " + data["reason"])
            }
        else:
            return {
                print("Erreur lors de la requête : " + str(response.status_code))
            }