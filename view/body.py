from PySide6.QtGui import QPixmap, QShortcut
from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, Signal
from view.meteo_widget.meteo_actuelle import MeteoAujourdhui
from view.meteo_widget.meteo_journee import MeteoJournee
from view.meteo_widget.meteo_semaine import MeteoSemaine


class RechercherUneVille(QWidget):
    ville_recherchee = Signal(str)
    def __init__(self,):
        super().__init__()

        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(0, 0, 0, 0)

        layout_input = QHBoxLayout()

        # Barre de recherche d'une ville
        self.input = QLineEdit()
        self.input.setPlaceholderText("Entrez une ville")
        self.input.setObjectName("inputVille")

        self.buttoninput = QPushButton("Rechercher")
        self.buttoninput.setObjectName("buttonInput")
        self.buttoninput.clicked.connect(self.button_rechercher)

        self.shortcut_enter = QShortcut(Qt.Key_Return, self)
        self.shortcut_enter.activated.connect(self.button_rechercher)

        layout_input.addWidget(self.input)
        layout_input.addWidget(self.buttoninput)

        layout_principal.addLayout(layout_input)

        # Connexion du signal de recherche de ville aux widgets météo
        self.ville_recherchee.connect(self.meteo_aujourdhui.set_ville)
        self.ville_recherchee.connect(self.meteo_journee.set_ville)
        self.ville_recherchee.connect(self.meteo_semaine.set_ville)

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
        print("Ville recherchée : ", nomville)

        self.ville_recherchee.emit(nomville)

        return nomville