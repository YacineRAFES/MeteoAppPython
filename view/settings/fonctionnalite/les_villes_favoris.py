from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QListWidget, QVBoxLayout, QTextEdit, \
    QListWidgetItem

from controllers.city_favourite_controller import CityFavouriteController


class FavouriteCity(QWidget):
    def __init__(self):
        super().__init__()
        self.city_name = "City Name"

        self.layout = QVBoxLayout()
        self.layout.addStretch()

        self.titre = QLabel("Villes favorites")
        self.titre.setObjectName("titreVillesFavoris")
        self.layout.addWidget(self.titre)

        self.layout_add_city = QHBoxLayout()

        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Ajouter une ville")
        self.input_text.setFixedHeight(30)
        self.layout_add_city.addWidget(self.input_text)

        self.button_add_city = QPushButton("Ajouter")
        self.button_add_city.setObjectName("buttonAddCity")
        self.layout_add_city.addWidget(self.button_add_city)

        self.layout_add_city.addStretch()

        self.button_add_city.clicked.connect(self.add_city)


        self.list_favorite_cities = QListWidget()

        item = QListWidgetItem(self.list_favorite_cities)
        button_remove = QPushButton("Supprimer")
        item.setSizeHint(button_remove.sizeHint())
        self.list_favorite_cities.setItemWidget(item, button_remove)

        self.layout.addLayout(self.layout_add_city)
        self.layout.addWidget(self.list_favorite_cities)

        self.layout.addStretch()

        self.setLayout(self.layout)

    def add_city(self):
        ville_a_ajouter = self.input_text.toPlainText()
        print("Ajouter une ville : ", ville_a_ajouter)
        if ville_a_ajouter:
            controller = CityFavouriteController()
            controller.AddCityFavourite(ville_a_ajouter)
