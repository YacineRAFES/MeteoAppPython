from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from view.settings.fonctionnalite.les_villes_favoris import FavouriteCity
from view.accueil.header import Header


class Parametre(QWidget):
    def __init__(self, main_header, parent=None):
        super().__init__(parent)

        layout_main = QVBoxLayout()

        # Ajoutez ici les éléments de votre page de paramètres
        titre_parametres = QLabel("Paramètres")
        titre_parametres.setObjectName("titreParametres")
        layout_main.addWidget(titre_parametres)

        les_villes_favoris = FavouriteCity(header_instance=main_header)

        layout_main.addWidget(les_villes_favoris)
        layout_main.addStretch()

        self.setLayout(layout_main)