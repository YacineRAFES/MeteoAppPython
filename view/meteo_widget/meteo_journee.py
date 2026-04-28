from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel



class MeteoJournee(QWidget):
    def __init__(self, nomville):
        super().__init__()
        self.nomville = nomville

        print("MeteoJournee : ", self.nomville)

        self.layout_principal = QVBoxLayout()
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_principal)

        self.meteoJourneeLayout = QHBoxLayout()

        meteoJournee = QWidget()
        meteoJournee.setObjectName("meteo_journee")
        meteoJournee.setLayout(self.meteoJourneeLayout)

        self.layout_principal.addWidget(meteoJournee)

    def maj_journee(self, hourly):

        for i in range(len(hourly.times)):
            icon, desc = hourly.get_weather_code(i)

            meteoHeure = QVBoxLayout()

            # Heure
            heure_label = QLabel(hourly.get_times(i))
            heure_label.setObjectName("meteoHeureLabel")
            heure_label.setAlignment(Qt.AlignCenter)
            meteoHeure.addWidget(heure_label)

            # Icône
            pixmap = QPixmap(icon)
            icons = QLabel("meteo_icon")
            icons.setPixmap(pixmap.scaled(200, 200))
            icons.setAlignment(Qt.AlignCenter)
            meteoHeure.addWidget(icons)

            # Température
            temp_label = QLabel(
                f"{hourly.get_temperatures(i)}°C"
            )
            temp_label.setObjectName("meteoTemp")
            temp_label.setAlignment(Qt.AlignCenter)
            meteoHeure.addWidget(temp_label)

            # Precipitation probabilité
            precip_label = QLabel(
                f"{hourly.get_precipitations(i)} %"
            )
            precip_label.setObjectName("precipProba")
            precip_label.setAlignment(Qt.AlignCenter)
            meteoHeure.addWidget(precip_label)

            self.meteoJourneeLayout.addLayout(meteoHeure)

    def vider(self):
        while self.meteoJourneeLayout.count():
            item = self.meteoJourneeLayout.takeAt(0)

            # C'est un layout (QVBoxLayout), pas un widget direct
            layout = item.layout()
            if layout is not None:
                # Supprimer tous les widgets du sous-layout
                while layout.count():
                    sous_item = layout.takeAt(0)
                    widget = sous_item.widget()
                    if widget is not None:
                        widget.deleteLater()
                # Supprimer le layout lui-même
                layout.deleteLater()

            # Au cas où il y aurait un widget direct
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()