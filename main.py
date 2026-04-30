import locale
import sys

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QStackedWidget

from view.accueil.accueil import Accueil
from view.settings.parametre import Parametre

locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
# On définit une classe de fenêtre par héritage.
class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.layout_main = None
        self.setWindowTitle("MeteoApp")
        self.resize(1600, 800)

        # menu de navigation
        menu_layout = QHBoxLayout()
        menu_layout.setContentsMargins(0, 0, 0, 10)
        menu_layout.setSpacing(0)

        bouton_accueil = QPushButton("Accueil")
        bouton_accueil.setObjectName("boutonMenu")
        bouton_accueil.clicked.connect(self.afficher_accueil)
        menu_layout.addWidget(bouton_accueil)

        bouton_settings = QPushButton("Paramètres")
        bouton_settings.setObjectName("boutonMenu")
        bouton_settings.clicked.connect(self.afficher_settings)
        menu_layout.addWidget(bouton_settings)

        menu_layout.addStretch()

        menu_widget = QWidget()
        menu_widget.setLayout(menu_layout)

        # QStackedWidget : une page visible à la fois
        self.stack = QStackedWidget()

        self.accueil_page = Accueil()
        self.settings_page = Parametre()

        self.stack.addWidget(self.accueil_page)   # index 0
        self.stack.addWidget(self.settings_page)  # index 1

        # assemblage du menu et du contenu dans la fenêtre principale
        assemblage_layout = QVBoxLayout()
        assemblage_layout.setContentsMargins(0, 0, 0, 0)
        assemblage_layout.setSpacing(0)
        assemblage_layout.addWidget(menu_widget)
        assemblage_layout.addWidget(self.stack)

        assemblage_layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(assemblage_layout)
        self.setCentralWidget(central_widget)

    # appelé pour afficher la page d'accueil
    def afficher_accueil(self):
        print("Affichage de la page d'accueil")
        self.stack.setCurrentIndex(0)

    # appelé pour afficher la page des paramètres
    def afficher_settings(self):
        print("Affichage de la page des paramètres")
        self.stack.setCurrentIndex(1)



if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    palette = QPalette()
    # Fond de l'application
    palette.setColor(QPalette.Window, QColor(187, 187, 187))
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