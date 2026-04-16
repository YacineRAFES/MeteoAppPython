from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from utilitaire.load_image_url import LoadImageUrl


class MeteoJournee(QWidget):
    def __init__(self, nomville):
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

    def maj_journee(self, hourly):

        for i in range(len(hourly.times)):
            icon, desc = hourly.get_weather_code(i)

            meteoHeure = QVBoxLayout()

            # Heure
            heure_label = QLabel(hourly.get_times(i))
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
            temp_label = QLabel(
                f"{hourly.get_temperatures(i)}°C"
            )
            temp_label.setObjectName("meteoTemp")
            meteoHeure.addWidget(temp_label)

            # Precipitation probabilité
            precip_label = QLabel(
                f"{hourly.get_precipitations(i)} %"
            )
            precip_label.setObjectName("precipProba")
            meteoHeure.addWidget(precip_label)

            self.meteoJourneeLayout.addLayout(meteoHeure)