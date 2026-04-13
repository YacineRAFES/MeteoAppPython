from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from api.weather_forecast.day_weather import DayWeather
from utilitaire.load_image_url import LoadImageUrl


class MeteoJournee(QWidget):
    def __init__(self, lat, lon, nomville):
        super().__init__()
        self.nomville = nomville

        print("MeteoJournee : ", self.nomville)

        self.layout_principal = QVBoxLayout()
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_principal)

        self.meteoJourneeLayout = QHBoxLayout()

        meteoJournee = QWidget()
        meteoJournee.setObjectName("meteo_journee")
        meteoJournee.setLayout(self.meteoJourneeLayout)

        self.layout_principal.addWidget(meteoJournee)

    @Slot(float, float, str)
    def set_ville(self, lat, lon, nomville):
        self.nomville = nomville

        # Récupère les données météo de la ville
        weather = DayWeather()
        dayweather = weather.get_day_weather(lat, lon)

        for time, icon, temp, proba in zip(
                dayweather["time"],
                dayweather["icon"],
                dayweather["temperature_2m"],
                dayweather["preci_proba"]
        ):
            meteoHeure = QVBoxLayout()

            # Heure
            heure_label = QLabel(str(time))
            heure_label.setObjectName("meteoHeureLabel")
            meteoHeure.addWidget(heure_label)

            # Icône
            image_data = LoadImageUrl().load_image_url(icon)
            if image_data:
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)
                icons = QLabel("meteo_icon")
                icons.setPixmap(pixmap.scaled(100, 100))
                meteoHeure.addWidget(icons)

            # Température
            temp_label = QLabel(str(temp) + "°C")
            temp_label.setObjectName("meteoTemp")
            meteoHeure.addWidget(temp_label)

            # Precipitation probabilité
            precip_label = QLabel(str(proba) + " %")
            precip_label.setObjectName("precipProba")
            meteoHeure.addWidget(precip_label)

            self.meteoJourneeLayout.addLayout(meteoHeure)