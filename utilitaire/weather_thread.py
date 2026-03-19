from PySide6.QtCore import QThread, Signal
from api.current_weather import current_weather


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
            results = current_weather().get_current_weather(self.ville)
            if results:
                self.finished.emit(self.ville, results)
            else:
                self.error.emit(self.ville, "Impossible de récupérer les données")
        except Exception as e:
            self.error.emit(self.ville, str(e))
