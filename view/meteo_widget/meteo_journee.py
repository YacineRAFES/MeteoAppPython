from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel


class MeteoJournee(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data

        meteoJourneeLayout = QHBoxLayout()

        for i in range(5):
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
        meteoJournee.setObjectName("meteoJournee")
        meteoJournee.setLayout(meteoJourneeLayout)