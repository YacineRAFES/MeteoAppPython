import json

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QCheckBox

from src.resources import resource_path

with resource_path("view","settings","fonctionnalite","weather_models.json").open(encoding="utf-8") as f:
    MODELS_DATA = json.load(f)

class WeatherModels(QWidget):
    def __init__(self, header_instance=None):
        super().__init__()
        self.header_instance = header_instance
        self.selected_models = []

        self.layout = QVBoxLayout()

        self.titre = QLabel("Weather Models")
        self.titre.setObjectName("weatherModels")
        self.layout.addWidget(self.titre)

        self.layout_add_city = QHBoxLayout()
        for provider, models in MODELS_DATA.items():
            provider_label = QLabel(provider)
            provider_label.setObjectName("providerLabel")
            self.layout.addWidget(provider_label)

            for model_name, model_id in models.items():
                checkbox = QCheckBox(model_name)
                checkbox.clicked.connect(
                    lambda checked, m_id=model_id, m_name=model_name: self.on_model_toggled(checked, m_id, m_name)
                )

        self.layout.addStretch()
        self.setLayout(self.layout)

    def on_model_toggled(self, checked, model_id, m_name):
        if checked:
            self.selected_models.append(model_id)
        else:
            if model_id in self.selected_models:
                self.selected_models.remove(model_id)
        print(self.selected_models)