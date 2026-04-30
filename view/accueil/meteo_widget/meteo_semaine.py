from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QLabel



class MeteoSemaine(QWidget):
    def __init__(self, nomville):
        super().__init__()
        self.nomville = nomville

        print("MeteoSemaine : ", self.nomville)

        self.layout_principal = QVBoxLayout()
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.layout_principal.addStretch()
        self.setLayout(self.layout_principal)

        # Affichage de la prévision météo sur 7 jours d'une ville recherchée
        self.meteo_semaine = QHBoxLayout()
        self.meteo_semaine.setObjectName("meteo_semaine")

    def maj_daily(self, daily):

        for i in range(len(daily.day)):
            icon, desc = daily.get_weather_code(i)

            meteo_jour_layout = QVBoxLayout()
            meteo_jour_layout.addStretch()

            meteo_jour_label = QLabel(
                f"{daily.get_day(i)}"
            )
            meteo_jour_label.setAlignment(Qt.AlignCenter)
            meteo_jour_label.setObjectName("meteo_jour_semaine")
            meteo_jour_layout.addWidget(meteo_jour_label)

            premier_colonne = QVBoxLayout()
            deuxieme_colonne = QVBoxLayout()

            deuxieme_colonne.addStretch()

            # Icône
            pixmap = QPixmap(icon)
            icons = QLabel("meteo_icon")
            icons.setPixmap(pixmap.scaled(200, 200))
            icons.setAlignment(Qt.AlignCenter)
            premier_colonne.addWidget(icons)

            meteo_temp_layout = QHBoxLayout()

            meteo_temp_layout.addStretch()

            meteo_temp_min = QLabel(
                f"{daily.get_temp_min(i)}°"
            )
            meteo_temp_min.setToolTip("Température minimale")
            meteo_temp_min.setObjectName("meteo_temp_semaine")
            meteo_temp_layout.addWidget(meteo_temp_min)

            meteo_temp_separateur = QLabel(" / ")
            meteo_temp_separateur.setObjectName("meteo_temp_semaine")
            meteo_temp_layout.addWidget(meteo_temp_separateur)

            meteo_temp_max = QLabel(
                f"{daily.get_temp_max(i)}°"
            )
            meteo_temp_max.setToolTip("Température maximale")
            meteo_temp_max.setObjectName("meteo_temp_semaine")
            meteo_temp_layout.addWidget(meteo_temp_max)

            meteo_temp_layout.addStretch()

            deuxieme_colonne.addLayout(meteo_temp_layout)

            # Precipitation probabilité
            meteo_preci_layout = QHBoxLayout()

            meteo_preci_layout.addStretch()

            icons_precipitation = QLabel()
            icons_precipitation.setObjectName("meteo_icon_precipitation")
            pixmap_precipitation = QPixmap("assets/precipitation.png")
            icons_precipitation.setPixmap(pixmap_precipitation.scaled(30, 30))
            meteo_preci_layout.addWidget(icons_precipitation)

            meteo_preci = QLabel(
                f" {daily.get_precipitations(i)} %"
            )
            meteo_preci.setObjectName("meteo_preci_semaine")
            meteo_preci.setAlignment(Qt.AlignCenter)
            meteo_preci.setToolTip("Probabilité de précipitation")
            meteo_preci_layout.addWidget(meteo_preci)

            meteo_preci_layout.addStretch()

            deuxieme_colonne.addLayout(meteo_preci_layout)

            deuxieme_colonne.addStretch()

            ligne_layout = QHBoxLayout()
            ligne_layout.addLayout(premier_colonne)
            ligne_layout.addLayout(deuxieme_colonne)

            meteo_jour_layout.addLayout(ligne_layout)

            meteo_jour = QWidget()
            meteo_jour.setObjectName("meteo_semaine")
            meteo_jour.setLayout(meteo_jour_layout)

            self.meteo_semaine.addWidget(meteo_jour)

        self.layout_principal.addLayout(self.meteo_semaine)

    def vider(self):
        while self.meteo_semaine.count():
            item = self.meteo_semaine.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()