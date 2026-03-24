from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class RechercherUneVille(QWidget):
    def __init__(self):
        super().__init__()


        layout_principal = QVBoxLayout()

        # Barre de recherche d'une ville
        input = QLineEdit()
        input.setPlaceholderText("Entrez une ville")
        input.setObjectName("inputVille")
        layout_principal.addWidget(input)

        # Affichage des données météo d'une ville recherchée
            # Affichage de la ville actuelle, de sa température et de son temps
        meteoActuelle = QHBoxLayout()
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

        # Affichage de la prévision météo sur les prochaines heures d'une ville recherchée

        meteoJournee = QHBoxLayout()
        for i in range(5):
            meteoHeure = QVBoxLayout()

            meteoHeureLabel = QLabel(f"{14 + i}h")
            meteoHeureLabel.setObjectName("meteoHeureLabel")
            meteoHeure.addWidget(meteoHeureLabel)

            icons = QLabel()
            pixmap = QPixmap("img.png")
            icons.setPixmap(pixmap.scaled(50, 50))
            meteoHeure.addWidget(icons)

            meteoTemp = QLabel(f"{25 + i}°C")
            meteoTemp.setObjectName("meteoTemp")
            meteoHeure.addWidget(meteoTemp)

            meteoHum = QLabel(f"Humidité : {60 - i * 5}%")
            meteoHum.setObjectName("meteoHum")
            meteoHeure.addWidget(meteoHum)

            meteoJournee.addLayout(meteoHeure)

        # Affichage de la prévision météo sur 7 jours d'une ville recherchée


        # Ajout des différentes parties au layout principal
        meteoActuelle.addLayout(meteoVilleDateIconTemp)
        meteoActuelle.addLayout(meteoTempsHumidity)
        layout_principal.addLayout(meteoActuelle)
        layout_principal.addLayout(meteoJournee)

        self.setLayout(layout_principal)