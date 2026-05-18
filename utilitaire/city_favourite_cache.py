from string import capwords
from threading import Lock
import pandas as pd
from pathlib import Path

from services.geo.geocoding import get_geo

CACHE_PATH = Path(__file__).parent.parent / "cache" / "favourite_city.csv"
_lock = Lock()

def add_city_favourite(nomville):

    with _lock:
        # Je vérifie si la ville existe dans le geocoding cache
        if CACHE_PATH.exists() and CACHE_PATH.stat().st_size > 0:
            print("add_city_favourite: Lecture de la liste des villes en favoris...")
            df = pd.read_csv(CACHE_PATH)
        else:
            print("add_city_favourite: favourite_city.csv, création d'un nouveau fichier csv...")
            df = pd.DataFrame(columns=["ville"])

        print("Recherche de la ville dans la liste..." + nomville)
        result = df[df["ville"] == capwords(nomville)]


        # Si la ville n'existe pas, je la rajoute dans le cache
        if result.empty:
            print("Ville non trouvée dans la liste, ajout en cours..." + nomville)
            new_row = {
                "ville": capwords(nomville)
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(CACHE_PATH, index=False)
            return new_row

        print("Ville trouvée dans la liste : " + nomville)
        return result.iloc[0].to_dict()

def get_favorite_cities():
    with _lock:
        if CACHE_PATH.exists() and CACHE_PATH.stat().st_size > 0:
            print("get_favorite_cities: Lecture de la liste des villes en favoris...")
            df = pd.read_csv(CACHE_PATH)
            return df["ville"].tolist()
        else:
            print("get_favorite_cities: favourite_city.csv, aucun favoris trouvé...")
            return []

def remove_favorite_cities(nomville):
    print("remove_favorite_cities : ", nomville)
    with _lock:
        if CACHE_PATH.exists() and CACHE_PATH.stat().st_size > 0:
            print("remove_favorite_cities: Lecture de la liste des villes en favoris...")
            df = pd.read_csv(CACHE_PATH)

            # Nettoyage et comparaison
            nom_nettoye = capwords(nomville.strip())
            condition = df["ville"].str.strip() == nom_nettoye

            # Si la ville existe bien dans le BDD
            if condition.any():
                # On garde tout SAUF cette ville
                df_modifie = df[~condition]

                # Sauvegarde dans le fichier CSV
                df_modifie.to_csv(CACHE_PATH, index=False)
                print(f"remove_favorite_cities: {nom_nettoye} supprimée du CSV.")
                return True
            else:
                print(f"remove_favorite_cities: {nom_nettoye} non trouvée dans le CSV.")
                return False
        else:
            print("remove_favorite_cities: favourite_city.csv, aucun favoris trouvé...")
            return False

