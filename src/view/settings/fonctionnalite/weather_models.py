import json

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QCheckBox

from src.resources import resource_path

with resource_path("view","settings","fonctionnalite","weather_models.json").open(encoding="utf-8") as f:
    MODELS_DATA = json.load(f)["weather_models"]

class WeatherModels(QWidget):
    def __init__(self, header_instance=None):
        super().__init__()
        self.header_instance = header_instance
        self.selected_models = []

        self.layout = QVBoxLayout()

        self.titre = QLabel("Weather Models")
        self.titre.setObjectName("weatherModels")
        self.layout.addWidget(self.titre)

        rangee = QHBoxLayout()
        rangee.setContentsMargins(0, 0, 0, 10)
        rangee_compteur = 0

        for fournisseur, modeles in MODELS_DATA.items():
            colonne = QVBoxLayout()

            fournisseur_label = QLabel(fournisseur)
            fournisseur_label.setObjectName("providerLabel")
            colonne.addWidget(fournisseur_label)

            for modeles_nom, modeles_id in modeles.items():
                checkbox = QCheckBox(modeles_nom)
                checkbox.clicked.connect(
                    lambda checked, m_id=modeles_id, m_name=modeles_nom: self.on_model_toggled(checked, m_id, m_name)
                )
                colonne.addWidget(checkbox)

            colonne.addStretch()
            rangee.addLayout(colonne)
            rangee_compteur += 1

            if rangee_compteur == 5:
            # Je crée un QVBoxLayout dans le layout_model
                self.layout.addLayout(rangee)
                rangee = QHBoxLayout()
                rangee.setContentsMargins(0, 0, 0, 10)
                rangee_compteur = 0

        if rangee_compteur > 0:
            rangee.addStretch()
            self.layout.addLayout(rangee)

        self.layout.addStretch()
        self.setLayout(self.layout)

    def on_model_toggled(self, checked, model_id, m_name):
        if checked:
            self.selected_models.append(model_id)
        else:
            if model_id in self.selected_models:
                self.selected_models.remove(model_id)
        print(self.selected_models)