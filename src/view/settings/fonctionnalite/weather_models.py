from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QRadioButton

class WeatherModels(QWidget):
    def __init__(self, header_instance=None):
        super().__init__()
        self.header_instance = header_instance

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