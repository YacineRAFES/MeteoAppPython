from PySide6.QtGui import QShortcut
from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt, Signal

from view.accueil.meteo_widget.meteo_actuelle import MeteoAujourdhui
from view.accueil.meteo_widget.meteo_journee import MeteoJournee
from view.accueil.meteo_widget.meteo_semaine import MeteoSemaine
from controllers.weather_controller import WeatherController

# TODO : Meteo Actuelle à revoir sur les styles (la taille de la police et les couleurs)
class Body(QWidget):
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
        self.meteo_aujourdhui = MeteoAujourdhui("")
        self.meteo_journee = MeteoJournee("")
        self.meteo_semaine = MeteoSemaine("")

        self.meteo_aujourdhui.setVisible(False)
        self.meteo_journee.setVisible(False)
        self.meteo_semaine.setVisible(False)

        # Layout pour la météo actuelle et la journée
        layout_meteo_AJ = QHBoxLayout()
        layout_meteo_AJ.addWidget(self.meteo_aujourdhui, 0)
        layout_meteo_AJ.addWidget(self.meteo_journee, 1)

        layout_principal.addLayout(layout_meteo_AJ)

        layout_principal.addWidget(self.meteo_semaine)
        layout_principal.addStretch()

        self.setLayout(layout_principal)

    def button_rechercher(self):
        nomville = self.input.text()
        print("Ville recherchée : ", nomville)

        controller = WeatherController(self)
        controller.load_weather(nomville)

        self.meteo_aujourdhui.setVisible(True)
        self.meteo_journee.setVisible(True)
        self.meteo_semaine.setVisible(True)

        return nomville