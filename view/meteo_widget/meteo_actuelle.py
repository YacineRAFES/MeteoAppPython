from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from utilitaire.load_image_url import LoadImageUrl

class MeteoAujourdhui(QWidget):
    def __init__(self, nomville):
        super().__init__()
        self.nomville = nomville

        print("MeteoAujourdhui : ", self.nomville)

        self.layout_principal = QVBoxLayout()
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_principal)

        # Affichage des données météo d'une ville recherchée
        meteoActuelleLayout = QHBoxLayout()
        meteoVilleDateIconTemp = QVBoxLayout()
        meteoTempsHumidity = QVBoxLayout()

        meteo_nom_ville = QLabel()
        meteo_nom_ville.setObjectName("meteo_nom_ville")
        meteoVilleDateIconTemp.addWidget(meteo_nom_ville)

        meteo_date_actuelle = QLabel()
        meteo_date_actuelle.setObjectName("meteo_date_actuelle")
        meteoVilleDateIconTemp.addWidget(meteo_date_actuelle)

        icons = QLabel()
        icons.setObjectName("meteo_icon")
        pixmap = QPixmap()
        icons.setPixmap(pixmap.scaled(100, 100))
        meteoVilleDateIconTemp.addWidget(icons)

        meteo_temperature = QLabel()
        meteo_temperature.setObjectName("meteo_temperature")
        meteoVilleDateIconTemp.addWidget(meteo_temperature)

        meteo_temps = QLabel()
        meteo_temps.setObjectName("meteo_temps")
        meteoTempsHumidity.addWidget(meteo_temps)

        meteo_humidity = QLabel()
        meteo_humidity.setObjectName("meteo_humidity")
        meteoTempsHumidity.addWidget(meteo_humidity)

        meteoActuelleLayout.addLayout(meteoVilleDateIconTemp)
        meteoActuelleLayout.addLayout(meteoTempsHumidity)

        meteo_actuelle = QWidget()
        meteo_actuelle.setObjectName("meteo_actuelle")
        meteo_actuelle.setLayout(meteoActuelleLayout)

        self.layout_principal.addWidget(meteo_actuelle)

    def maj_current(self, current, nomville):
        icon, desc = current.get_weather_code

        # met à jour les labels avec les données récupérées
        # Nom de la ville
        self.findChild(QLabel, "meteo_nom_ville").setText(
            nomville.capitalize()
        )
        # Date de la dernière mise à jour
        self.findChild(QLabel, "meteo_date_actuelle").setText(
            "Dernière mise à jour : " + current.get_time()
        )

        # Icone météo
        image_data = LoadImageUrl().load_image_url(icon)
        if image_data:
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            self.findChild(QLabel, "meteo_icon").setPixmap(pixmap.scaled(100, 100))

        # Température actuelle
        self.findChild(QLabel, "meteo_temperature").setText(
            f"{current.get_temperature()}°C"
        )

        # Description du temps (ensoleillé, nuageux, etc.)
        self.findChild(QLabel, "meteo_temps").setText(
            desc
        )
        # Humidité
        self.findChild(QLabel, "meteo_humidity").setText(
            f"Humidité : {current.get_humidity()}%"
        )

    def vider(self):
        self.findChild(QLabel, "meteo_nom_ville").setText("")
        self.findChild(QLabel, "meteo_date_actuelle").setText("")
        self.findChild(QLabel, "meteo_icon").setPixmap(QPixmap())
        self.findChild(QLabel, "meteo_temperature").setText("")
        self.findChild(QLabel, "meteo_temps").setText("")
        self.findChild(QLabel, "meteo_humidity").setText("")