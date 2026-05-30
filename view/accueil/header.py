from pathlib import Path
import pandas as pd
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QScrollArea, QScroller
from PySide6.QtCore import Qt

from utilitaire.weather_thread import WeatherThread

class Header(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)

        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout_principal)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QScrollArea.NoFrame)
        QScroller.grabGesture(self.scroll_area, QScroller.LeftMouseButtonGesture)
        layout_principal.addWidget(self.scroll_area)

        # Initialisation du layout principal
        self.conteneur_scroll = QWidget()
        self.layout_meteoInternational = QHBoxLayout()
        self.layout_meteoInternational.setContentsMargins(10, 10, 10, 10)
        self.layout_meteoInternational.setSpacing(15)
        self.conteneur_scroll.setLayout(self.layout_meteoInternational)

        self.scroll_area.setWidget(self.conteneur_scroll)

        self.loading_label = None
        self.worker = []

        self.setFixedHeight(230)

        # Premier chargement au lancement du widget
        self.charger_meteo()

    def charger_meteo(self):
        """Méthode unique pour vider l'ancien affichage et lancer les threads"""
        # 1. Nettoyage complet du layout (utilisé lors du refresh)
        while self.layout_meteoInternational.count() > 0:
            item = self.layout_meteoInternational.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # 2. Création et affichage du label de chargement
        self.loading_label = QLabel("Chargement...")
        self.loading_label.setObjectName("loadingLabel")
        self.layout_meteoInternational.addWidget(self.loading_label)

        # 3. Arrêt et vidage des anciens workers
        self.worker.clear()

        # 4. Récupération et lancement des nouveaux threads
        villes = self.get_villes()
        if not villes:
            self.loading_label.setText("Aucune ville dans les favoris.")
            return

        for ville in villes:
            worker = WeatherThread(ville)
            worker.finished.connect(self.on_weather_loaded)
            worker.error.connect(self.on_weather_error)
            self.worker.append(worker)
            worker.start()

    def refresh(self):
        """Appelé depuis l'extérieur pour rafraîchir la liste"""
        print("Header: Rafraîchissement de la météo des favoris...")
        self.charger_meteo()

    def on_weather_loaded(self, ville, results):
        """Appelé quand les données météo sont prêtes"""
        # Masquer le chargement dès qu'une première ville répond
        if self.loading_label and self.loading_label.parent():
            self.loading_label.deleteLater()
            self.loading_label = None

        icon, desc = results.get_weather_code

        ville_widget = QWidget()
        ville_widget.setObjectName("widgetVille")

        layout_ville = QVBoxLayout()
        ville_widget.setLayout(layout_ville)

        # Afficher les données
        self.header_du_bloc(layout_ville, results.city, results.code_country)
        self.corps_du_bloc(layout_ville, str(results.get_temperature()), desc, icon)

        self.layout_meteoInternational.addWidget(ville_widget)
        self.layout_meteoInternational.setAlignment(Qt.AlignCenter)

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
            code_label = QLabel(f"({code_country})")
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
        FAVOURITE_CITY = Path(__file__).parent.parent.parent / "cache" / "favorites_city.csv"

        # Si le fichier n'existe pas encore ou il est vide
        if not FAVOURITE_CITY.exists() or FAVOURITE_CITY.stat().st_size == 0:
            return []

        df = pd.read_csv(FAVOURITE_CITY)
        return df[["id", "ville", "pays", "region", "departement", "municipale", "latitude", "longitude", "code_country"]].to_dict('records')