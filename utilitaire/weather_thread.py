from PySide6.QtCore import QThread, Signal

from services.weather.current_weather import CurrentWeather
from utilitaire.geocoding_cache import get_geocoding


class WeatherThread(QThread):
    """Traitement qui récupère la météo d'une ville sans bloquer l'interface"""

    # Il signale si la récupération est terminée avec succès, en envoyant les données météo
    finished = Signal(str, dict)
    # Il signale s'il y a une erreur, en envoyant un message d'erreur
    error = Signal(str, str)

    def __init__(self, ville):
        super().__init__()
        self.ville = ville

    def run(self):
        try:
            # Récupérer les coordonnées
            geo = get_geocoding(self.ville)
            if not geo:
                self.error.emit(self.ville, "Géocodage impossible")
                return

            # Récupérer la météo avec les coordonnées
            weather = CurrentWeather()
            results = weather.get_current_weather(geo["latitude"], geo["longitude"])
            if not results:
                self.error.emit(self.ville, "Météo indisponible")
                return

            # Fusionner les données
            results["code_country"] = geo["code_country"]

            self.finished.emit(self.ville, results)
        except Exception as e:
            self.error.emit(self.ville, str(e))
