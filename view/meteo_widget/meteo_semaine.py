from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QLabel


class MeteoSemaine(QWidget):
    def __init__(self, nomville):
        super().__init__()
        self.nomville = nomville

        self.layout_principal = QVBoxLayout()
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_principal)

        # Affichage de la prévision météo sur 7 jours d'une ville recherchée
        meteoSemaine = QHBoxLayout()
        meteoSemaine.setObjectName("meteoSemaine")
        for i in range(7):
            meteoJourLayout = QVBoxLayout()

            meteoJourLabel = QLabel(f"Jour {i + 1}")
            meteoJourLabel.setObjectName("meteoJourLabel")
            meteoJourLayout.addWidget(meteoJourLabel)

            icons = QLabel()
            pixmap = QPixmap("img.png")
            icons.setPixmap(pixmap.scaled(50, 50))
            meteoJourLayout.addWidget(icons)

            meteoTemp = QLabel(f"{25 + i}°C")
            meteoTemp.setObjectName("meteoTemp")
            meteoJourLayout.addWidget(meteoTemp)

            meteoHum = QLabel(f"Humidité : {60 - i * 5}%")
            meteoHum.setObjectName("meteoHum")
            meteoJourLayout.addWidget(meteoHum)

            meteoJour = QWidget()
            meteoJour.setObjectName("meteoJour")
            meteoJour.setLayout(meteoJourLayout)

            meteoSemaine.addWidget(meteoJour)


        self.layout_principal.addLayout(meteoSemaine)