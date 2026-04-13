from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QLabel

from api.weather_forecast.week_weather import WeekWeather
from utilitaire.load_image_url import LoadImageUrl


class MeteoSemaine(QWidget):
    def __init__(self, nomville):
        super().__init__()
        self.nomville = nomville

        print("MeteoSemaine : ", self.nomville)

        self.layout_principal = QVBoxLayout()
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.layout_principal.addStretch()
        self.setLayout(self.layout_principal)

        # Affichage de la prévision météo sur 7 jours d'une ville recherchée
        self.meteo_semaine = QHBoxLayout()
        self.meteo_semaine.setObjectName("meteo_semaine")

    @Slot(float, float, str)
    def set_ville(self, lat, lon, nomville):
        self.nomville = nomville

        # Récupère les données météo de la ville
        weather = WeekWeather()
        week_weather = weather.get_week_weather(lat, lon)

        for time, icon, temp_min, temp_max, proba in zip(
                week_weather["time"],
                week_weather["icon"],
                week_weather["temperature_min"],
                week_weather["temperature_max"],
                week_weather["preci_proba"]):

            meteo_jour_layout = QVBoxLayout()
            meteo_jour_layout.addStretch()

            meteo_jour_label = QLabel(str(time))
            meteo_jour_label.setAlignment(Qt.AlignCenter)
            meteo_jour_label.setObjectName("meteo_jour_label")
            meteo_jour_layout.addWidget(meteo_jour_label)

            # Icône
            image_data = LoadImageUrl().load_image_url(icon)
            if image_data:
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)
                icons = QLabel("meteo_icon")
                icons.setPixmap(pixmap.scaled(100, 100))
                meteo_jour_layout.addWidget(icons)

            meteo_temp_layout = QHBoxLayout()

            meteo_temp_min = QLabel(str(temp_min))
            meteo_temp_min.setObjectName("meteo_temp_min")
            meteo_temp_layout.addWidget(meteo_temp_min)

            meteo_temp_max = QLabel(str(temp_max)+"°C")
            meteo_temp_max.setObjectName("meteo_temp_max")
            meteo_temp_layout.addWidget(meteo_temp_max)

            meteo_jour_layout.addLayout(meteo_temp_layout)

            meteo_preci = QLabel(f"Précip' prob' : " + str(proba) + " %")
            meteo_preci.setObjectName("meteo_preci")
            meteo_jour_layout.addWidget(meteo_preci)

            meteo_jour = QWidget()
            meteo_jour.setObjectName("meteo_semaine")
            meteo_jour.setLayout(meteo_jour_layout)

            self.meteo_semaine.addWidget(meteo_jour)

        self.layout_principal.addLayout(self.meteo_semaine)