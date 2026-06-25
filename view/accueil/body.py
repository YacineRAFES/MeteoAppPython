from PySide6.QtGui import QShortcut
from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QSizePolicy
from PySide6.QtCore import Qt, Signal

from utilitaire.msg_box import message_box_geocoding, message_box
from view.accueil.meteo_widget.meteo_actuelle import MeteoAujourdhui
from view.accueil.meteo_widget.meteo_aujourd_charts import MeteoAujourdhuiCharts
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
        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Entrez une ville")
        self.input_text.setObjectName("inputVille")

        # Position de la barre de recherche au centre
        layout_input.setAlignment(Qt.AlignCenter)
        layout_input.setContentsMargins(0, 20, 0, 10)

        # réduire la taille de la barre de recherche
        self.input_text.setFixedWidth(300)

        self.buttoninput = QPushButton("Rechercher")
        self.buttoninput.setObjectName("buttonInput")
        self.buttoninput.clicked.connect(self.button_rechercher)

        # réduire la taille de bouton de recherche
        self.buttoninput.setFixedWidth(100)


        self.shortcut_enter = QShortcut(Qt.Key_Return, self)
        self.shortcut_enter.activated.connect(self.button_rechercher)

        layout_input.addWidget(self.input_text)
        layout_input.addWidget(self.buttoninput)

        layout_principal.addLayout(layout_input)
        layout_principal.addStretch(1)

        # Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setMinimumHeight(400)
        scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        scroll_area.setObjectName("scrollArea")

        # Conteneur Meteo pour meteo_actuelle, meteo_journee, meteo_semaire
        meteo_conteneur = QWidget()
        meteo_conteneur.setObjectName("meteo_conteneur")

        layout_meteo = QVBoxLayout(meteo_conteneur)

        # Ajout des différentes parties au layout principal
        self.meteo_aujourdhui = MeteoAujourdhui("")
        self.meteo_aujourd_charts = MeteoAujourdhuiCharts()
        self.meteo_journee = MeteoJournee("")
        self.meteo_semaine = MeteoSemaine("")

        self.meteo_aujourdhui.setVisible(False)
        self.meteo_journee.setVisible(False)
        self.meteo_semaine.setVisible(False)
        self.meteo_aujourd_charts.setVisible(False)

        # Layout pour la météo actuelle et la journée
        layout_meteo_AJ = QHBoxLayout()
        layout_meteo_AJ.addWidget(self.meteo_aujourdhui, 0)
        layout_meteo_AJ.addWidget(self.meteo_journee, 1)

        layout_meteo.addLayout(layout_meteo_AJ)
        layout_meteo.addWidget(self.meteo_aujourd_charts)
        layout_meteo.addWidget(self.meteo_semaine)

        scroll_area.setWidget(meteo_conteneur)

        layout_principal.addWidget(scroll_area)

        self.setLayout(layout_principal)

    def button_rechercher(self):
        nomville = self.input_text.text()
        print("Ville recherchée : ", nomville)

        controller = WeatherController(self)
        result_geocoding = controller.load_weather(nomville, "Search")

        # Verifie le message de controller
        if not result_geocoding["erreur"]:
            ville_selectionner = message_box_geocoding(result_geocoding["data"])
            self.input_text.clear()
        else:
            print(result_geocoding["erreur"] + result_geocoding["message"])
            message_box(result_geocoding["message"])
            return

        if ville_selectionner:
            controller.load_weather(ville_selectionner, "Choice")
        else:
            print("La sélection est vide, donc return")
            return

        self.meteo_aujourdhui.setVisible(True)
        self.meteo_journee.setVisible(True)
        self.meteo_semaine.setVisible(True)
        self.meteo_aujourd_charts.setVisible(True)