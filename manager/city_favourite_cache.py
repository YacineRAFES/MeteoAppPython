from string import capwords
from threading import Lock
import pandas as pd
from pathlib import Path

from services.geo.geocoding import get_geo
from utilitaire.gestion_erreur import gestion_erreur

FAVORITES_CITY = Path(__file__).parent.parent / "cache" / "favorites_city.csv"
_lock = Lock()

def add_favorite_city(nomville):

    with _lock:
        # Je vérifie si la ville existe dans le FAVORITES_CITY
        if FAVORITES_CITY.exists() and FAVORITES_CITY.stat().st_size > 0:
            print("add_city_favourite: Lecture de la liste des villes en favoris...")
            df = pd.read_csv(FAVORITES_CITY)
        else:
            print("add_city_favourite: favorites_city.csv, création d'un nouveau fichier csv...")
            df = pd.DataFrame(columns=["ville"])

        print("Recherche de la ville dans la liste..." + nomville)
        resultat_apres_la_recherche = df[df["ville"] == capwords(nomville)]


        # Si la ville n'existe pas, je la rajoute dans le FAVOURITE_CITY
        if resultat_apres_la_recherche.empty:

            print("Ville non trouvée dans la liste, ajout en cours..." + nomville)

            new_row = {
                "ville": capwords(nomville)
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(FAVORITES_CITY, index=False)

            return True

        print("Ville trouvée dans la liste : " + nomville)
        return False

def get_favorite_cities():
    with _lock:
        if FAVORITES_CITY.exists() and FAVORITES_CITY.stat().st_size > 0:
            print("get_favorite_cities: Lecture de la liste des villes en favoris...")
            df = pd.read_csv(FAVORITES_CITY)
            return df["ville"].tolist()
        else:
            print("get_favorite_cities: favorites_city.csv, aucun favoris trouvé...")
            return []

def remove_favorite_cities(nomville):
    print("remove_favorite_cities : ", nomville)
    with _lock:
        if FAVORITES_CITY.exists() and FAVORITES_CITY.stat().st_size > 0:
            print("remove_favorite_cities: Lecture de la liste des villes en favoris...")
            df = pd.read_csv(FAVORITES_CITY)

            # Nettoyage et comparaison
            nom_nettoye = capwords(nomville.strip())
            condition = df["ville"].str.strip() == nom_nettoye

            # Si la ville existe bien dans le BDD
            if condition.any():
                # On garde tout SAUF cette ville
                df_modifie = df[~condition]

                # Sauvegarde dans le fichier CSV
                df_modifie.to_csv(FAVORITES_CITY, index=False)
                print(f"remove_favorite_cities: {nom_nettoye} supprimée du CSV.")
                return True
            else:
                print(f"remove_favorite_cities: {nom_nettoye} non trouvée dans le CSV.")
                return False
        else:
            print("remove_favorite_cities: favorites_city.csv, aucun favoris trouvé...")
            return False

