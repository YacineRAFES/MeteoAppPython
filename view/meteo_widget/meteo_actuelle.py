from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from api.geocoding import GeoCoding
from api.current_weather import CurrentWeather

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

        meteoNomVille = QLabel("Ville")
        meteoNomVille.setObjectName("meteoNomVille")
        meteoVilleDateIconTemp.addWidget(meteoNomVille)

        meteoDateActuelle = QLabel("mardi 25 juin 2024 à 14:00")
        meteoDateActuelle.setObjectName("meteoDateActuelle")
        meteoVilleDateIconTemp.addWidget(meteoDateActuelle)

        icons = QLabel()
        pixmap = QPixmap("img.png")
        icons.setPixmap(pixmap.scaled(100, 100))
        meteoVilleDateIconTemp.addWidget(icons)

        meteoTemperature = QLabel("25°C")
        meteoTemperature.setObjectName("meteoTemperature")
        meteoVilleDateIconTemp.addWidget(meteoTemperature)

        meteoTemps = QLabel("Ensoleillé")
        meteoTemps.setObjectName("meteoTemps")
        meteoTempsHumidity.addWidget(meteoTemps)

        meteoHumidity = QLabel("Humidité : 60%")
        meteoHumidity.setObjectName("meteoHumidity")
        meteoTempsHumidity.addWidget(meteoHumidity)

        meteoActuelleLayout.addLayout(meteoVilleDateIconTemp)
        meteoActuelleLayout.addLayout(meteoTempsHumidity)

        meteoActuelle = QWidget()
        meteoActuelle.setObjectName("meteoActuelle")
        meteoActuelle.setLayout(meteoActuelleLayout)

        self.layout_principal.addWidget(meteoActuelle)

    @Slot(str)
    def set_ville(self, nomville):
        self.nomville = nomville

        # appel api
        # recupère la geolocalisation de la ville
        geo = GeoCoding()
        geocoding = geo.GetGeo(nomville)
        # recupère les données météo de la ville
        weather = CurrentWeather()
        current_weather = weather.GetCurrentWeather(geocoding["latitude"], geocoding["longitude"])

        # met à jour les labels avec les données récupérées
        self.findChild(QLabel, "meteoNomVille").setText(nomville)
        self.findChild(QLabel, "meteoDateActuelle").setText("mardi 25 juin 2024 à 14:00")
        self.findChild(QLabel, "meteoTemperature").setText(f"{current_weather['temperature_2m']}°C")
        self.findChild(QLabel, "meteoTemps").setText(current_weather["description"])
        self.findChild(QLabel, "meteoHumidity").setText(f"Humidité : {current_weather['humidity']}%")

