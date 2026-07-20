from src.modele.current_model import WeatherCurrent
from src.modele.daily_model import WeatherDaily
from src.modele.hourly_model import WeatherHourly
from src.services.geo.geocoding import get_geocoding
from src.services.weather.weather_api import fetch_weather
from src.services.weather.weather_parser import parse_current, parse_hourly, parse_daily



class WeatherController:
    def __init__(self, view):
        self.view = view

    def load_weather(self, value, action):
        print(f"Appel depuis le controllers load_weather pour {value}")
        if action == "Search":
            # Appel géocoding
            geo = get_geocoding(value)
            if not geo:
                print("probleme de geocoding")
                return {
                    "erreur": True,
                    "message": "Probleme de geocoding"
                }

            else:
                print("requete geocoding recu")
                return {
                    "erreur": False,
                    "data": geo
                }
        if action == "Choice":

            # Appel API
            data = fetch_weather(value["latitude"], value["longitude"])
            # if not data:
            #     view.show_error("Erreur API")
            #     return

            # Parsing
            current_data = parse_current(data)
            hourly_data = parse_hourly(data)
            daily_data = parse_daily(data)

            # Modèle
            current = WeatherCurrent(current_data)
            hourly = WeatherHourly(hourly_data)
            daily = WeatherDaily(daily_data)

            # Vider les données précédentes
            self.view.meteo_aujourdhui.vider() # appel du widget meteo_actuelle.py
            self.view.meteo_journee.vider() # appel du widget meteo_journee.py
            self.view.meteo_journee_charts.vider()
            self.view.meteo_semaine.vider() # appel du widget meteo_semaine.py

            # Mise à jour UI
            self.view.meteo_aujourdhui.maj_current(current, value["city"]) # appel du widget meteo_actuelle.py
            self.view.meteo_journee.maj_journee(hourly) # appel du widget meteo_journee.py
            self.view.meteo_journee_charts.maj_charts_temperature(hourly)
            self.view.meteo_journee_charts.maj_charts_precipitation(hourly)
            self.view.meteo_semaine.maj_daily(daily) # appel du widget meteo_semaine.py