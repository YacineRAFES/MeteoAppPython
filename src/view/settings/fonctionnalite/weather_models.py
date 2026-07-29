import json

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QRadioButton

from src.resources import resource_path

with resource_path("view","settings","fonctionnalite","weather_models.json").open(encoding="utf-8") as f:
    MODELS_DATA = json.load(f)

class WeatherModels(QWidget):
    def __init__(self, header_instance=None):
        super().__init__()
        self.header_instance = header_instance
        print(MODELS_DATA)
        self.layout = QVBoxLayout()
        self.layout.addStretch()

        self.titre = QLabel("Weather Models")
        self.titre.setObjectName("weatherModels")
        self.layout.addWidget(self.titre)

        self.layout_add_city = QHBoxLayout()


        self.button_radio = QRadioButton("test")
        self.button_radio = QRadioButton("test")

        self.layout.addWidget(self.button_radio)

        self.setLayout(self.layout)