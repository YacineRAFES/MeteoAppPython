import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QHBoxLayout
from PySide6.QtCore import Qt
from view.header.les_villes_internationales import villes_international


# On définit une classe de fenêtre par héritage.
class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MeteoApp")
        self.resize(1600, 800)

        layout_main = QVBoxLayout()
        layout_main.setAlignment(Qt.AlignTop)
        layout_meteoInternational = QHBoxLayout()

        for i in range(7):

            layout_meteoInternational.addWidget(villes_international(ville[i], code_country[i], temperature[i], temps[i]))


        layout_main.addLayout(layout_meteoInternational)

        layout_main.addStretch()


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