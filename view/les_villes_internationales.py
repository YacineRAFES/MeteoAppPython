from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

from utilitaire.weather_thread import WeatherThread

VILLES = ["Paris", "New York", "Tokyo", "Quebec", "Londres", "Berlin", "Amsterdam"]

class VilleWidget(QWidget):
    def __init__(self, ville):
        super().__init__()
        self.ville = ville
        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)

        # Afficher un état de chargement
        self.header_du_bloc(ville, "")
        self.loading_label = QLabel("Chargement...")
        self.loading_label.setObjectName("loadingLabel")
        self.layout_principal.addWidget(self.loading_label)

        # Lancer le thread pour récupérer les données
        self.worker = WeatherThread(ville)
        self.worker.finished.connect(self.on_weather_loaded)
        self.worker.error.connect(self.on_weather_error)
        self.worker.start()

    def on_weather_loaded(self, ville, results):
        """Appelé quand les données météo sont prêtes"""
        # Supprimer le label de chargement
        self.loading_label.deleteLater()

        # Afficher les données
        self.corps_du_bloc(str(results["temperature_2m"]) + "°C", results["description"])

    def on_weather_error(self, ville, error_message):
        """Appelé en cas d'erreur"""
        self.loading_label.setText(f"Erreur: {error_message}")

    def header_du_bloc(self, ville, code_country):
        layout_nomville_codecountry = QHBoxLayout()
        layout_nomville_codecountry.setAlignment(Qt.AlignLeft)

        nomville = QLabel(ville)
        nomville.setObjectName("nomville")
        layout_nomville_codecountry.addWidget(nomville)

        if code_country:
            code_label = QLabel(f"({code_country})")
            code_label.setObjectName("code_country")
            layout_nomville_codecountry.addWidget(code_label)

        self.layout_principal.addLayout(layout_nomville_codecountry)

    def corps_du_bloc(self, temperature, temps):
        layout_icons_temp = QHBoxLayout()
        layout_icons_temp.setAlignment(Qt.AlignLeft)

        layout_icons = QVBoxLayout()
        layout_temp_temps = QVBoxLayout()

        icons = QLabel()
        pixmap = QPixmap("img.png")
        icons.setPixmap(pixmap.scaled(100, 100))
        layout_icons.addWidget(icons)

        temp = QLabel(temperature)
        temp.setObjectName("tempLabel")
        layout_temp_temps.addWidget(temp)

        temps_label = QLabel(temps)
        temps_label.setObjectName("tempsLabel")
        layout_temp_temps.addWidget(temps_label)

        layout_icons_temp.addLayout(layout_icons)
        layout_icons_temp.addLayout(layout_temp_temps)

        self.layout_principal.addLayout(layout_icons_temp)
