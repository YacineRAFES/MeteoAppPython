from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class Parametre(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout_main = QVBoxLayout()
        # Ajoutez ici les éléments de votre page de paramètres
        titre_parametres = QLabel("Paramètres")
        titre_parametres.setObjectName("titreParametres")
        layout_main.addWidget(titre_parametres)

        self.setLayout(layout_main)