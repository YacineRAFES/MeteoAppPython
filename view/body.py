from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from view.meteo_widget.meteo_actuelle import MeteoAujourdhui
from view.meteo_widget.meteo_journee import MeteoJournee
from view.meteo_widget.meteo_semaine import MeteoSemaine


class RechercherUneVille(QWidget):
    def __init__(self,):
        super().__init__()

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

        # Ajout des différentes parties au layout principal
        self.meteo_aujourdhui = MeteoAujourdhui(nomville="")
        self.meteo_journee = MeteoJournee(nomville="")
        self.meteo_semaine = MeteoSemaine(nomville="")

        layout_principal.addWidget(self.meteo_aujourdhui)
        layout_principal.addWidget(self.meteo_journee)
        layout_principal.addWidget(self.meteo_semaine)

        self.setLayout(layout_principal)
    def button_rechercher(self):
        nomville = self.input.text()

        return nomville