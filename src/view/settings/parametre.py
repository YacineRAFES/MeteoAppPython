from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QScrollArea

from src.view.settings.fonctionnalite.les_villes_favoris import FavouriteCity
from src.view.settings.fonctionnalite.weather_models import WeatherModels


class Parametre(QWidget):
    def __init__(self, main_header, parent=None):
        super().__init__(parent)

        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout_principal)

        # Widget conteneur qui ira DANS la scrollarea
        contenu = QWidget()
        layout_contenu = QVBoxLayout()
        contenu.setLayout(layout_contenu)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(contenu)  # <-- l'étape qui manquait
        layout_principal.addWidget(self.scroll_area)

        layout_ligne_un = QHBoxLayout()
        layout_ligne_deux = QHBoxLayout()

        titre_parametres = QLabel("Paramètres")
        titre_parametres.setObjectName("titreParametres")
        layout_contenu.addWidget(titre_parametres)  # <-- ajouté au contenu, pas au layout_principal

        les_villes_favoris = FavouriteCity(header_instance=main_header)
        weather_models = WeatherModels(header_instance=main_header)

        layout_ligne_un.addWidget(les_villes_favoris)
        layout_ligne_un.addStretch()

        layout_ligne_deux.addWidget(weather_models)

        layout_contenu.addLayout(layout_ligne_un)
        layout_contenu.addLayout(layout_ligne_deux)

        layout_contenu.addStretch()