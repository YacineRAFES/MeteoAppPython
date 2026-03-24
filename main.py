import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtCore import Qt

from view.body import RechercherUneVille
from view.les_villes_internationales import VilleWidget, VILLES


# On définit une classe de fenêtre par héritage.
class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MeteoApp")
        self.resize(1600, 800)

        layout_main = QVBoxLayout()
        layout_main.setAlignment(Qt.AlignTop)
        layout_meteoInternational = QHBoxLayout()

        for ville in VILLES:
            widget_ville = VilleWidget(ville)
            layout_meteoInternational.addWidget(widget_ville)

        layout_main.addLayout(layout_meteoInternational)
        layout_main.addStretch()

        body_meteo = RechercherUneVille()
        layout_main.addWidget(body_meteo)

        central_widget = QWidget()
        central_widget.setLayout(layout_main)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # On instancie une fenêtre graphique et l'affiche.
    myWindow = MyWindow()
    myWindow.show()

    with open('style.qss', 'r') as f:
        style = f.read()

    app.setStyleSheet(style)

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())