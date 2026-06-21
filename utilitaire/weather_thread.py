from PySide6.QtCore import QThread, Signal
from manager.city_favourite_cache import get_favorite_cities
from modele.current_model import WeatherCurrent
from services.weather.weather_api import fetch_weather_for_list_cities
from services.weather.weather_parser import parse_already_current


class WeatherThread(QThread):
    finished = Signal(str, object)
    error = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.villes_data = get_favorite_cities()

    def run(self):
        try:
            data = fetch_weather_for_list_cities(self.villes_data)
            if not data:
                for city in self.villes_data:
                    self.error.emit(city["ville"], "Météo indisponible")
                return

            for i, city in enumerate(self.villes_data):
                try:
                    city_weather = data[i]
                    current_data = city_weather["current"]

                    parsed_current = parse_already_current(current_data)
                    current = WeatherCurrent(parsed_current)
                    current.city = city["ville"]
                    current.code_country = city["code_country"]

                    self.finished.emit(city["ville"], current)

                except Exception as e:
                    self.error.emit(city["ville"], f"Erreur de parsing: {str(e)}")

        except Exception as e:
            for city in self.villes_data:
                self.error.emit(city["ville"], f"Erreur API: {str(e)}")