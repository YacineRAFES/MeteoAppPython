from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QLabel

from services.weather.week_weather import WeekWeather
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

    def maj_daily(self, daily):

        for i in range(len(daily.times)):
            icon, desc = daily.get_weather_code(i)

            meteo_jour_layout = QVBoxLayout()
            meteo_jour_layout.addStretch()

            meteo_jour_label = QLabel(
                f"{daily.get_times(i)}"
            )
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

            meteo_temp_min = QLabel(
                f"{daily.get_temp_min(i)}°C"
            )
            meteo_temp_min.setObjectName("meteo_temp_min")
            meteo_temp_layout.addWidget(meteo_temp_min)

            meteo_temp_max = QLabel(
                f"{daily.get_temp_max(i)}°C"
            )
            meteo_temp_max.setObjectName("meteo_temp_max")
            meteo_temp_layout.addWidget(meteo_temp_max)

            meteo_jour_layout.addLayout(meteo_temp_layout)

            meteo_preci = QLabel(
                f"{daily.get_precipitations(i)} %"
            )
            meteo_preci.setObjectName("meteo_preci")
            meteo_jour_layout.addWidget(meteo_preci)

            meteo_jour = QWidget()
            meteo_jour.setObjectName("meteo_semaine")
            meteo_jour.setLayout(meteo_jour_layout)

            self.meteo_semaine.addWidget(meteo_jour)

        self.layout_principal.addLayout(self.meteo_semaine)