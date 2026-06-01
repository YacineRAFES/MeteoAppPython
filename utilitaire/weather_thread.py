from PySide6.QtCore import QThread, Signal

from modele.current_model import WeatherCurrent
from services.weather.weather_api import fetch_weather
from services.weather.weather_parser import parse_current


class WeatherThread(QThread):
    """Traitement qui récupère la météo d'une ville sans bloquer l'interface"""

    # Il signale si la récupération est terminée avec succès, en envoyant les données météo
    finished = Signal(str, object)
    # Il signale s'il y a une erreur, en envoyant un message d'erreur
    error = Signal(str, str)

    def __init__(self, ville_data):
        super().__init__()
        self.ville = ville_data["ville"]
        self.code_country = ville_data["code_country"]
        self.latitude = ville_data["latitude"]
        self.longitude = ville_data["longitude"]
        print(self.ville, self.latitude, self.longitude)


    def run(self):
        try:
            # Récupérer la météo avec les coordonnées
            data = fetch_weather(self.latitude, self.longitude)
            current_data = parse_current(data)
            current = WeatherCurrent(current_data)
            if not current:
                self.error.emit(self.ville, "Météo indisponible")
                return

            # Fusionner les données
            current.city = self.ville
            current.code_country = self.code_country

            self.finished.emit(self.ville, current)
        except Exception as e:
            self.error.emit(self.ville, str(e))
