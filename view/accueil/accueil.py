from PySide6.QtWidgets import QVBoxLayout, QWidget

from view.accueil.body import Body
from view.accueil.header import Header


class Accueil(QWidget):
    def __init__(self, /):

        super().__init__()
        layout_main = QVBoxLayout()

        # Affichage des villes internationales
        header = Header()
        layout_main.addWidget(header)

        # Affichage de la barre de recherche d'une ville
        body = Body()
        layout_main.addWidget(body)

        layout_main.addStretch()

        self.setLayout(layout_main)
