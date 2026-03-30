from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt


class RechercherUneVille(QWidget):
    def __init__(self,):
        super().__init__()

        self.buttoninput = None
        layout_principal = QVBoxLayout()

        layout_input = QHBoxLayout()

        # Barre de recherche d'une ville
        self.input = QLineEdit()
        self.input.setPlaceholderText("Entrez une ville")
        self.input.setObjectName("inputVille")

        self.buttoninput = QPushButton("Rechercher")
        self.buttoninput.setObjectName("buttonInput")
        self.buttoninput.clicked.connect(self.button_rechercher)

        layout_input.addWidget(self.input)
        layout_input.addWidget(self.buttoninput)

        layout_principal.addLayout(layout_input)



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

        # Affichage de la prévision météo sur les prochaines heures d'une ville recherchée

        meteoJourneeLayout = QHBoxLayout()

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

            meteoJourneeLayout.addLayout(meteoHeure)

        meteoJournee = QWidget()
        meteoJournee.setObjectName("meteoJournee")
        meteoJournee.setLayout(meteoJourneeLayout)

        # Affichage de la prévision météo sur 7 jours d'une ville recherchée
        meteoSemaine = QHBoxLayout()
        meteoSemaine.setObjectName("meteoSemaine")
        for i in range(7):
            meteoJourLayout = QVBoxLayout()

            meteoJourLabel = QLabel(f"Jour {i + 1}")
            meteoJourLabel.setObjectName("meteoJourLabel")
            meteoJourLayout.addWidget(meteoJourLabel)

            icons = QLabel()
            pixmap = QPixmap("img.png")
            icons.setPixmap(pixmap.scaled(50, 50))
            meteoJourLayout.addWidget(icons)

            meteoTemp = QLabel(f"{25 + i}°C")
            meteoTemp.setObjectName("meteoTemp")
            meteoJourLayout.addWidget(meteoTemp)

            meteoHum = QLabel(f"Humidité : {60 - i * 5}%")
            meteoHum.setObjectName("meteoHum")
            meteoJourLayout.addWidget(meteoHum)

            meteoJour = QWidget()
            meteoJour.setObjectName("meteoJour")
            meteoJour.setLayout(meteoJourLayout)

            meteoSemaine.addWidget(meteoJour)

        # Ajout des différentes parties au layout principal
        layout_principal.addWidget(meteoActuelle)
        layout_principal.addWidget(meteoJournee)
        layout_principal.addLayout(meteoSemaine)

        self.setLayout(layout_principal)
    def button_rechercher(self):
        nomVille = self.input.text()
        print(f"Recherche de la ville : {nomVille}")