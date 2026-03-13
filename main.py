import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QHBoxLayout
from PySide6.QtCore import Qt


# On définit une classe de fenêtre par héritage.
class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MeteoApp")
        self.resize(1280, 800)

        layout_main = QVBoxLayout()
        layout_main.setAlignment(Qt.AlignTop)
        layout_meteoInternational = QHBoxLayout()

        for i in range(6):
            bloc_ville = QWidget()
            bloc_ville.setObjectName("bloc_ville")

            bloc_vertical = QVBoxLayout()

            # l'entete du bloc, on a l'icons de la météo et la température
            layout_icons_temp = QHBoxLayout()
            layout_icons_temp.setAlignment(Qt.AlignLeft)


            icons = QLabel()
            pixmap = QPixmap("img.png")
            icons.setPixmap(pixmap)
            icons.setPixmap(pixmap.scaled(100, 100))
            layout_icons_temp.addWidget(icons)

            temp = QLabel("20°C")
            temp.setObjectName("tempLabel")
            layout_icons_temp.addWidget(temp)

            # un layout pour le nom de la ville et le code country (FR) (UK) etc..

            layout_nomville_codecountry = QHBoxLayout()
            layout_nomville_codecountry.setAlignment(Qt.AlignLeft)

            nomville = QLabel("Nomville")
            nomville.setObjectName("nomville")
            layout_nomville_codecountry.addWidget(nomville)

            code_country = QLabel("(FR)")
            code_country.setObjectName("code_country")
            layout_nomville_codecountry.addWidget(code_country)

            bloc_vertical.addLayout(layout_nomville_codecountry)
            bloc_vertical.addLayout(layout_icons_temp)

            bloc_ville.setLayout(bloc_vertical)



            layout_meteoInternational.addWidget(bloc_ville)


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