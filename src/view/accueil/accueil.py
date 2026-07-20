from PySide6.QtWidgets import QVBoxLayout, QWidget

from src.view.accueil.body import Body


class Accueil(QWidget):
    def __init__(self, header_instance):

        super().__init__()
        layout_main = QVBoxLayout()

        # Affichage des villes internationales
        self.header = header_instance
        layout_main.addWidget(self.header)

        # Affichage de la barre de recherche d'une ville
        body = Body()
        layout_main.addWidget(body, 1)


        self.setLayout(layout_main)
