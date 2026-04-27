from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy


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

        premiere_colonne = QVBoxLayout()
        deuxieme_colonne = QVBoxLayout()
        deuxieme_colonne.addStretch()

        meteo_nom_ville = QLabel()
        meteo_nom_ville.setObjectName("meteo_nom_ville")
        premiere_colonne.addWidget(meteo_nom_ville)

        icons = QLabel()
        icons.setObjectName("meteo_icon")
        pixmap = QPixmap()
        icons.setPixmap(pixmap.scaled(200, 200))
        premiere_colonne.addWidget(icons)

        meteo_temps = QLabel()
        meteo_temps.setObjectName("meteo_temps")
        deuxieme_colonne.addWidget(meteo_temps)

        meteo_temperature = QLabel()
        meteo_temperature.setObjectName("meteo_temperature")
        deuxieme_colonne.addWidget(meteo_temperature)

        meteo_humidity = QLabel()
        meteo_humidity.setObjectName("meteo_humidity")
        deuxieme_colonne.addWidget(meteo_humidity)

        deuxieme_colonne.addStretch()

        meteoActuelleLayout.addLayout(premiere_colonne)
        meteoActuelleLayout.addLayout(deuxieme_colonne)

        meteoActuelleLayout.addStretch()

        meteo_actuelle = QWidget()
        meteo_actuelle.setObjectName("meteo_actuelle")
        meteo_actuelle.setLayout(meteoActuelleLayout)

        self.layout_principal.addWidget(meteo_actuelle)
        self.layout_principal.addStretch()

    def maj_current(self, current, nomville):
        icon, desc = current.get_weather_code

        # met à jour les labels avec les données récupérées
        # Nom de la ville
        self.findChild(QLabel, "meteo_nom_ville").setText(
            nomville.capitalize()
        )

        # Icone météo
        pixmap = QPixmap(icon)
        self.findChild(QLabel, "meteo_icon").setPixmap(pixmap.scaled(300, 300))

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
            f"{current.get_humidity()}%"
        )

    def vider(self):
        self.findChild(QLabel, "meteo_nom_ville").setText("")
        self.findChild(QLabel, "meteo_icon").setPixmap(QPixmap())
        self.findChild(QLabel, "meteo_temperature").setText("")
        self.findChild(QLabel, "meteo_temps").setText("")
        self.findChild(QLabel, "meteo_humidity").setText("")