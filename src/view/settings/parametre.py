from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout

from src.view.settings.fonctionnalite.les_villes_favoris import FavouriteCity


class Parametre(QWidget):
    def __init__(self, main_header, parent=None):
        super().__init__(parent)

        layout_main = QVBoxLayout()
        layout_ligne_un = QHBoxLayout()

        # Ajoutez ici les éléments de votre page de paramètres
        titre_parametres = QLabel("Paramètres")
        titre_parametres.setObjectName("titreParametres")
        layout_main.addWidget(titre_parametres)

        les_villes_favoris = FavouriteCity(header_instance=main_header)

        layout_ligne_un.addWidget(les_villes_favoris)
        layout_ligne_un.addStretch()

        layout_main.addLayout(layout_ligne_un)

        self.setLayout(layout_main)