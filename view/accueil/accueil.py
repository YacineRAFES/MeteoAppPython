from PySide6.QtWidgets import QVBoxLayout, QWidget

from view.accueil.body import Body
from view.accueil.header import Header


class Accueil(QWidget):
    def __init__(self, header_instance):

        super().__init__()
        layout_main = QVBoxLayout()

        # Affichage des villes internationales
        self.header = header_instance
        layout_main.addWidget(self.header)

        # Affichage de la barre de recherche d'une ville
        body = Body()
        layout_main.addWidget(body)

        layout_main.addStretch()

        self.setLayout(layout_main)
