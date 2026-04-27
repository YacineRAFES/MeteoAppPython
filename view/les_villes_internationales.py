from pathlib import Path

import pandas as pd
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

from utilitaire.weather_thread import WeatherThread
from utilitaire.load_image_url import LoadImageUrl

class VilleWidget(QWidget):
    # TODO : Si une ou des villes internationales n'a été affiché, on refait l'opération
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.layout_meteoInternational = QHBoxLayout()
        self.layout_meteoInternational.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_meteoInternational)

        # Afficher un état de chargement
        self.loading_label = QLabel("Chargement...")
        self.loading_label.setObjectName("loadingLabel")
        self.layout_meteoInternational.addWidget(self.loading_label)

        self.worker = []

        VILLES = self.get_villes()

        for ville in VILLES:
            # Lancer le thread pour récupérer les données
            worker = WeatherThread(ville)
            worker.finished.connect(self.on_weather_loaded)
            worker.error.connect(self.on_weather_error)
            self.worker.append(worker)
            worker.start()

    def on_weather_loaded(self, ville, results):
        """Appelé quand les données météo sont prêtes"""
        # Supprimer le label de chargement
        if self.loading_label and self.loading_label.parent():
            self.loading_label.deleteLater()
            self.loading_label = None

        icon, desc = results.get_weather_code

        ville_widget = QWidget()
        ville_widget.setObjectName("widgetVille")

        layout_ville = QVBoxLayout()
        ville_widget.setLayout(layout_ville)

        # Afficher les données
        self.header_du_bloc(layout_ville, ville, results.code_country)
        self.corps_du_bloc(layout_ville, str(results.get_temperature()), desc, icon)

        self.layout_meteoInternational.addWidget(ville_widget)

    def on_weather_error(self, ville, error_message):
        """Appelé en cas d'erreur"""
        if self.loading_label and self.loading_label.parent():
            self.loading_label.setText(f"Erreur: {error_message}, ville: {ville}")

    def header_du_bloc(self, layout_ville, ville, code_country):
        layout_nomville_codecountry = QHBoxLayout()
        layout_nomville_codecountry.setAlignment(Qt.AlignLeft)

        nomville = QLabel(ville)
        nomville.setObjectName("nomville")
        layout_nomville_codecountry.addWidget(nomville)

        if code_country:
            code_label = QLabel("("+code_country+")")
            code_label.setObjectName("code_country")
            layout_nomville_codecountry.addWidget(code_label)

        layout_ville.addLayout(layout_nomville_codecountry)



    def corps_du_bloc(self, layout_ville, temperature, temps, icon):
        layout_icons_temp = QHBoxLayout()
        layout_icons_temp.setAlignment(Qt.AlignLeft)

        layout_icons = QVBoxLayout()
        layout_temp_temps = QVBoxLayout()

        icons = QLabel()

        pixmap = QPixmap(icon)
        if not pixmap.isNull():
            icons.setPixmap(pixmap.scaled(200, 200))
        layout_icons.addWidget(icons)

        temp = QLabel(temperature + "°C")
        temp.setObjectName("tempLabel")
        layout_temp_temps.addWidget(temp)

        temps_label = QLabel(temps)
        temps_label.setObjectName("tempsLabel")
        temps_label.setWordWrap(True)
        layout_temp_temps.addWidget(temps_label)

        layout_icons_temp.addLayout(layout_icons)
        layout_icons_temp.addLayout(layout_temp_temps)

        layout_ville.addLayout(layout_icons_temp)

    def get_villes(self):
        INTERNATIONAL_FILE = Path(__file__).parent.parent / "cache" / "villes_international.csv"
        df = pd.read_csv(INTERNATIONAL_FILE)

        return df["ville"].tolist()
