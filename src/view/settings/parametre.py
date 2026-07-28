from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout

from src.view.settings.fonctionnalite.les_villes_favoris import FavouriteCity
from src.view.settings.fonctionnalite.weather_models import WeatherModels


class Parametre(QWidget):
    def __init__(self, main_header, parent=None):
        super().__init__(parent)

        layout_main = QVBoxLayout()
        layout_ligne_un = QHBoxLayout()
        layout_ligne_deux = QHBoxLayout()

        # Ajoutez ici les éléments de votre page de paramètres
        titre_parametres = QLabel("Paramètres")
        titre_parametres.setObjectName("titreParametres")
        layout_main.addWidget(titre_parametres)

        les_villes_favoris = FavouriteCity(header_instance=main_header)
        weather_models = WeatherModels(header_instance=main_header)
        # Ajout les paramètres pour °C et °F


        layout_ligne_un.addWidget(les_villes_favoris)
        layout_ligne_un.addStretch()

        layout_ligne_deux.addWidget(weather_models)

        layout_main.addLayout(layout_ligne_un)
        layout_main.addLayout(layout_ligne_deux)

        layout_main.addStretch()

        self.setLayout(layout_main)