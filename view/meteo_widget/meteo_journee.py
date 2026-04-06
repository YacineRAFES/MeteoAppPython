from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel


class MeteoJournee(QWidget):
    def __init__(self, lat, lon, nomville):
        super().__init__()
        self.nomville = nomville

        print("MeteoJournee : ", self.nomville)

        self.layout_principal = QVBoxLayout()
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_principal)

        meteoJourneeLayout = QHBoxLayout()

        for i in range(12):
            meteoHeure = QVBoxLayout()

            meteoHeureLabel = QLabel(f"{14 + i}h")
            meteoHeureLabel.setObjectName("meteoHeureLabel")
            meteoHeure.addWidget(meteoHeureLabel)

            icons = QLabel()
            pixmap = QPixmap("img.png")
            icons.setPixmap(pixmap.scaled(50, 50))
            meteoHeure.addWidget(icons)

            meteoTemp = QLabel(f"{25 + i}°C")
            meteoTemp.setObjectName("meteoTemp")
            meteoHeure.addWidget(meteoTemp)

            meteoHum = QLabel(f"Humidité : {60 - i * 5}%")
            meteoHum.setObjectName("meteoHum")
            meteoHeure.addWidget(meteoHum)

            meteoJourneeLayout.addLayout(meteoHeure)

        meteoJournee = QWidget()
        meteoJournee.setObjectName("meteo_journee")
        meteoJournee.setLayout(meteoJourneeLayout)

        self.layout_principal.addWidget(meteoJournee)

    @Slot(str)
    def set_ville(self, nomville):

        self.nomville = nomville
        # appel api