from string import capwords

from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QListWidget, QVBoxLayout, QTextEdit, \
    QListWidgetItem, QMessageBox, QLineEdit

from controllers.favorites_city_controller import CityFavouriteController
from utilitaire.msg_box import message_box


class FavouriteCity(QWidget):
    def __init__(self, header_instance=None):
        super().__init__()
        self.header_instance = header_instance
        self.city_name = "City Name"

        self.layout = QVBoxLayout()
        self.layout.addStretch()

        self.titre = QLabel("Villes favorites")
        self.titre.setObjectName("titreVillesFavoris")
        self.layout.addWidget(self.titre)

        self.layout_add_city = QHBoxLayout()
        self.layout_add_city.addStretch()

        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Ajouter une ville")
        self.input_text.setFixedHeight(30)
        self.layout_add_city.addWidget(self.input_text)

        self.button_add_city = QPushButton("Ajouter")
        self.button_add_city.setObjectName("buttonAddCity")
        self.layout_add_city.addWidget(self.button_add_city)

        self.layout_add_city.addStretch()

        self.button_add_city.clicked.connect(self.add_city)

        self.shortcut_enter = QShortcut(QKeySequence("Return"), self)
        self.shortcut_enter.activated.connect(self.add_city)

        # Layout : Listes des villes et les boutons supprimer, modifier.
        self.layout_liste_villes = QHBoxLayout()

        # Création de la liste
        self.liste_widget = QListWidget()

        # Appel au controller pour récupérer la liste des villes en favoris
        controller = CityFavouriteController()
        villes_favoris = controller.GetFavoriteCities()

        # Ajout les villes dans la liste
        self.liste_widget.addItems(villes_favoris)

        # Ajout le WidgetList dans la layout
        self.layout_liste_villes.addWidget(self.liste_widget)

        # Créer des boutons : supprimer, modifier
        # Création un layout pour les boutons
        self.layout_boutons = QVBoxLayout()

        # Bouton Supprimer
        supprimer_bouton = QPushButton('Supprimer')
        supprimer_bouton.clicked.connect(self.supprimer)

        # Assemblages des widget dans le layout des boutons
        self.layout_boutons.addWidget(supprimer_bouton)

        # Ajout le layout des boutons dans la layout des listes
        self.layout_liste_villes.addLayout(self.layout_boutons)


        # -- Assemblage des layouts dans la layout principale --
        self.layout.addLayout(self.layout_add_city)
        self.layout.addLayout(self.layout_liste_villes)

        self.layout.addStretch()

        self.setLayout(self.layout)

    def add_city(self):
        ville_a_ajouter = self.input_text.text()
        print("Ajouter une ville : ", ville_a_ajouter)
        if ville_a_ajouter:
            controller = CityFavouriteController()
            controller.AddCityFavourite(ville_a_ajouter)

            # ajoute dans la liste
            self.liste_widget.addItem(capwords(ville_a_ajouter))
            self.input_text.clear()

            if self.header_instance:
                self.header_instance.refresh()

    def supprimer(self):
        print("appel au suppression d'une ville")
        ligne_selectionner = self.liste_widget.currentRow()
        if ligne_selectionner >= 0:
            objet_actuel = self.liste_widget.item(ligne_selectionner)

            # Appel au controller pour la suppression dans le CSV
            controller = CityFavouriteController()
            controller.RemoveCityFavourite(objet_actuel)

            # supprime dans la liste
            self.liste_widget.takeItem(ligne_selectionner)
            self.input_text.clear()

            if self.header_instance:
                self.header_instance.refresh()

