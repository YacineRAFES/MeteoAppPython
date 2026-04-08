from PySide6.QtGui import QShortcut
from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt, Signal

from utilitaire.geocoding_cache import get_geocoding
from view.meteo_widget.meteo_actuelle import MeteoAujourdhui
from view.meteo_widget.meteo_journee import MeteoJournee
from view.meteo_widget.meteo_semaine import MeteoSemaine

# TODO : Meteo Actuelle à revoir sur les styles (la taille de la police et les couleurs)
# TODO : Meteo Journee à faire
# TODO : Meteo Semaine à faire


class RechercherUneVille(QWidget):
    ville_recherchee = Signal(float, float, str)
    def __init__(self):
        super().__init__()

        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(0, 0, 0, 0)

        layout_input = QHBoxLayout()

        # Barre de recherche d'une ville
        self.input = QLineEdit()
        self.input.setPlaceholderText("Entrez une ville")
        self.input.setObjectName("inputVille")

        # Position de la barre de recherche au centre
        layout_input.setAlignment(Qt.AlignCenter)
        layout_input.setContentsMargins(0, 20, 0, 10)

        # réduire la taille de la barre de recherche
        self.input.setFixedWidth(300)

        self.buttoninput = QPushButton("Rechercher")
        self.buttoninput.setObjectName("buttonInput")
        self.buttoninput.clicked.connect(self.button_rechercher)

        # réduire la taille de bouton de recherche
        self.buttoninput.setFixedWidth(100)


        self.shortcut_enter = QShortcut(Qt.Key_Return, self)
        self.shortcut_enter.activated.connect(self.button_rechercher)

        layout_input.addWidget(self.input)
        layout_input.addWidget(self.buttoninput)

        layout_principal.addLayout(layout_input)


        # Ajout des différentes parties au layout principal
        self.meteo_aujourdhui = MeteoAujourdhui(0, 0, "")
        self.meteo_journee = MeteoJournee(0, 0, "")
        self.meteo_semaine = MeteoSemaine(0, 0, "")

        self.meteo_aujourdhui.setVisible(False)
        self.meteo_journee.setVisible(False)
        self.meteo_semaine.setVisible(False)

        # Connexion du signal de recherche de ville aux widgets météo
        self.ville_recherchee.connect(self.meteo_aujourdhui.set_ville)
        self.ville_recherchee.connect(self.meteo_journee.set_ville)
        self.ville_recherchee.connect(self.meteo_semaine.set_ville)

        layout_principal.addWidget(self.meteo_aujourdhui)
        layout_principal.addWidget(self.meteo_journee)
        layout_principal.addWidget(self.meteo_semaine)



        self.setLayout(layout_principal)
    def button_rechercher(self):
        nomville = self.input.text()
        print("Ville recherchée : ", nomville)

        #appel  api
        # geocoding pour récupérer les coordonnées de la ville
        geocoding = get_geocoding(nomville)

        self.ville_recherchee.emit(geocoding["latitude"], geocoding["longitude"], nomville)

        self.meteo_aujourdhui.setVisible(True)
        self.meteo_journee.setVisible(True)
        self.meteo_semaine.setVisible(True)

        return nomville