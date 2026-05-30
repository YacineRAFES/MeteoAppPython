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

    def __init__(self, ville):
        super().__init__()
        self.ville = ville


    def run(self):
        try:
            # Récupérer la météo avec les coordonnées
            data = fetch_weather(self.ville["latitude"], self.ville["longitude"])
            current_data = parse_current(data)
            current = WeatherCurrent(current_data)
            if not current:
                self.error.emit(self.ville, "Météo indisponible")
                return

            # Fusionner les données
            current.code_country = self.ville["code_country"]

            self.finished.emit(self.ville, current)
        except Exception as e:
            self.error.emit(self.ville, str(e))
