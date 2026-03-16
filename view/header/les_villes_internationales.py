from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class villes_international(QWidget):
    def __init__(self, ville, code_country, temperature, temps):
        super().__init__()

    def header_du_bloc(self, ville, code_country):
        layout_nomville_codecountry = QHBoxLayout()
        layout_nomville_codecountry.setAlignment(Qt.AlignLeft)

        nomville = QLabel("Nomville")
        nomville.setObjectName("nomville")
        layout_nomville_codecountry.addWidget(nomville)

        code_country = QLabel("(FR)")
        code_country.setObjectName("code_country")
        layout_nomville_codecountry.addWidget(code_country)

        self.addLayout(layout_nomville_codecountry)

    def corps_du_bloc(self, temperature, temps):

        layout_icons_temp = QHBoxLayout()
        layout_icons_temp.setAlignment(Qt.AlignLeft)

        layout_icons = QVBoxLayout()
        layout_temp_temps = QVBoxLayout()

        icons = QLabel()
        pixmap = QPixmap("img.png")
        icons.setPixmap(pixmap)
        icons.setPixmap(pixmap.scaled(100, 100))
        layout_icons.addWidget(icons)

        temp = QLabel("20°C")
        temp.setObjectName("tempLabel")
        layout_temp_temps.addWidget(temp)

        temps = QLabel("Nuageux")
        temps.setObjectName("tempsLabel")
        layout_temp_temps.addWidget(temps)

        layout_icons_temp.addLayout(layout_icons)
        layout_icons_temp.addLayout(layout_temp_temps)
