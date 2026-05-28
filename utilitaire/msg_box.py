from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMessageBox, QHBoxLayout, QLabel, QPushButton, QGridLayout, QWidget, QDialog

def message_box(message):
    msgBox = QMessageBox()
    msgBox.setText(message)
    msgBox.exec()

def message_box_geocoding(data):
    fenetre = QDialog()
    fenetre.setWindowTitle("Sélection de la ville")

    layout = QGridLayout(fenetre)

    for i in range(data):
        pixmap = QPixmap("assets/01d@2x.png")
        icon = QLabel()
        icon.setPixmap(pixmap.scaled(32, 32))
        layout.addWidget(icon, i, 0)

        layout.addWidget(QLabel(data["ville"]), i, 1)
        layout.addWidget(QLabel(data["code_country"]), i, 2)
        layout.addWidget(QLabel(data["pays"]), i, 3)
        layout.addWidget(QLabel(data["latitude"]), i, 4)
        layout.addWidget(QLabel(data["longitude"]), i, 5)

        bouton = QPushButton("Choisir")
        bouton.clicked.connect(fenetre.accept)
        layout.addWidget(bouton, i, 6)

    fenetre.exec()