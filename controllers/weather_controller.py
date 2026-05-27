from modele.current_model import WeatherCurrent
from modele.daily_model import WeatherDaily
from modele.hourly_model import WeatherHourly
from services.geo.geocoding import get_geocoding
from services.weather.weather_api import fetch_weather
from services.weather.weather_parser import parse_current, parse_hourly, parse_daily



class WeatherController:
    def __init__(self, view):
        self.view = view

    def load_weather(self, nomville):
        print(f"Appel depuis le controllers load_weather pour {nomville}...")

        # Appel géocoding
        geo = get_geocoding(nomville)

        for ville in geo:
            nom = ville["city"]
            pays = ville["country"]

            print(f" {nom} ({pays}) ")

        print(geo)
        # # Appel API
        # data = fetch_weather(geo["latitude"], geo["longitude"])
        # # if not data:
        # #     view.show_error("Erreur API")
        # #     return
        #
        # # Parsing
        # current_data = parse_current(data)
        # hourly_data = parse_hourly(data)
        # daily_data = parse_daily(data)
        #
        # # Modèle
        # current = WeatherCurrent(current_data)
        # hourly = WeatherHourly(hourly_data)
        # daily = WeatherDaily(daily_data)
        #
        # # Vider les données précédentes
        # self.view.meteo_aujourdhui.vider() # appel du widget meteo_actuelle.py
        # self.view.meteo_journee.vider() # appel du widget meteo_journee.py
        # self.view.meteo_semaine.vider() # appel du widget meteo_semaine.py
        #
        # # Mise à jour UI
        # self.view.meteo_aujourdhui.maj_current(current, nomville) # appel du widget meteo_actuelle.py
        # self.view.meteo_journee.maj_journee(hourly) # appel du widget meteo_journee.py
        # self.view.meteo_semaine.maj_daily(daily) # appel du widget meteo_semaine.py