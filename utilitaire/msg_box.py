from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMessageBox, QHBoxLayout, QLabel, QPushButton, QGridLayout, QWidget, QDialog


def message_box(message):
    msgBox = QMessageBox()
    msgBox.setText(message)
    msgBox.exec()

def message_box_geocoding():
    fenetre = QDialog()
    fenetre.setWindowTitle("Sélection de la ville")

    layout = QGridLayout(fenetre)

    for i in range(5):
        pixmap = QPixmap("assets/01d@2x.png")
        icon = QLabel()
        icon.setPixmap(pixmap.scaled(32, 32))
        layout.addWidget(icon, i, 0)

        layout.addWidget(QLabel("NomVille"), i, 1)
        layout.addWidget(QLabel("FR"), i, 2)
        layout.addWidget(QLabel("France"), i, 3)
        layout.addWidget(QLabel("48.85°"), i, 4)
        layout.addWidget(QLabel("2.35°"), i, 5)

        bouton = QPushButton("Choisir")
        bouton.clicked.connect(fenetre.accept)
        layout.addWidget(bouton, i, 6)

    fenetre.exec()