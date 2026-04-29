import locale
import sys

from PySide6.QtGui import QPalette, QColor, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QPushButton

from view.body import RechercherUneVille
from view.les_villes_internationales import VilleWidget


locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
# On définit une classe de fenêtre par héritage.
class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MeteoApp")
        self.resize(1600, 800)

        # menu de navigation
        menu_layout = QHBoxLayout()
        menu_layout.setContentsMargins(0, 0, 0, 10)
        menu_layout.setSpacing(0)

        bouton_accueil = QPushButton("Accueil")
        bouton_accueil.setObjectName("boutonMenu")
        menu_layout.addWidget(bouton_accueil)
        menu_layout.addStretch()

        menu_widget = QWidget()
        menu_widget.setLayout(menu_layout)

        # contenu affichage de la page d'accueil
        layout_main = QVBoxLayout()

        widget_ville = VilleWidget()

        layout_main.addWidget(widget_ville)

        body_meteo = RechercherUneVille()
        layout_main.addWidget(body_meteo)
        layout_main.addStretch()

        contenu_widget = QWidget()
        contenu_widget.setLayout(layout_main)

        # assemblage du menu et du contenu dans la fenêtre principale
        assemblage_layout = QVBoxLayout()
        assemblage_layout.setContentsMargins(0, 0, 0, 0)
        assemblage_layout.setSpacing(0)
        assemblage_layout.addWidget(menu_widget)
        assemblage_layout.addWidget(contenu_widget)

        assemblage_layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(assemblage_layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    palette = QPalette()
    # Fond de l'application
    palette.setColor(QPalette.Window, QColor(0, 0, 0))
    # Texte noir
    palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
    # Fond des widgets
    palette.setColor(QPalette.Base, QColor(255, 255, 255))
    # Texte des widgets
    palette.setColor(QPalette.Text, QColor(0, 0, 0))
    # Boutons gris clair
    palette.setColor(QPalette.Button, QColor(240, 240, 240))
    # Texte des boutons
    palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
    app.setPalette(palette)

    # On instancie une fenêtre graphique et l'affiche.
    myWindow = MyWindow()
    myWindow.show()


    with open('style.qss', 'r') as f:
        style = f.read()

    app.setStyleSheet(style)

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())