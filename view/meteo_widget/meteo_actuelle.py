from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel

class MeteoAujourdhui(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data

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

