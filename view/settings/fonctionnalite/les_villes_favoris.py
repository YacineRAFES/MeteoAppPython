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

        controller = CityFavouriteController()
        self.villes_favoris = controller.GetFavoriteCities()

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

        # Ajout les villes dans la liste
        self.liste_widget.addItems(self.villes_favoris)

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
        # On récupère le nom de la ville saisie et on l'enregistre dans la variable
        ville_a_ajouter = self.input_text.text().strip().lower()
        print("Ajouter une ville : ", ville_a_ajouter)

        # Si la saisie est vide, on annule
        if not ville_a_ajouter:
            print("La saisie est vide, donc return")
            return

        # On enregistre les villes existantes qui se trouve dans la liste widget dans une array
        liste_widget_villes = []
        for i in range(self.liste_widget.count()):
            liste_widget_villes = self.liste_widget.item(i).text().lower()

        # On vérifie si la ville saisie existe dans la liste de widgets, si la ville saisie existe donc on return
        if ville_a_ajouter.lower() in liste_widget_villes:
            print("La ville existe déjà dans la liste widgets")
            return

        # -- Appel au controller --
        controller = CityFavouriteController()
        sauvegarde_resultat = controller.AddCityFavourite(ville_a_ajouter)

        if not sauvegarde_resultat["erreur"]:
            self.liste_widget.addItem(capwords(ville_a_ajouter))
            self.input_text.clear()
            message_box(sauvegarde_resultat["message"])
        else:
            message_box(sauvegarde_resultat["message"])

        # ajoute dans la liste

        if self.header_instance:
            self.header_instance.refresh()

    def supprimer(self):
        print("appel au suppression d'une ville")
        ligne_selectionner = self.liste_widget.currentRow()
        if ligne_selectionner >= 0:
            objet_actuel = self.liste_widget.item(ligne_selectionner)

            # Appel au controller pour la suppression dans le CSV
            controller = CityFavouriteController()
            suppression_resultat = controller.RemoveCityFavourite(objet_actuel)

            if not suppression_resultat["erreur"]:
                # supprime dans la liste
                self.liste_widget.takeItem(ligne_selectionner)
                self.input_text.clear()
                message_box(suppression_resultat["message"])

                if self.header_instance:
                    self.header_instance.refresh()
            else:
                message_box(suppression_resultat["message"])
