from string import capwords
from threading import Lock
import pandas as pd
from pathlib import Path


FAVORITES_CITY = Path(__file__).parent.parent / "cache" / "favorites_city.csv"
_lock = Lock()

def add_favorite_city(value):

    with _lock:
        # Je vérifie si la ville existe dans le FAVORITES_CITY
        if FAVORITES_CITY.exists() and FAVORITES_CITY.stat().st_size > 0:
            print("add_city_favourite: Lecture de la liste des villes en favoris...")
            df = pd.read_csv(FAVORITES_CITY)
        else:
            print("add_city_favourite: favorites_city.csv, création d'un nouveau fichier csv...")
            df = pd.DataFrame(
                columns=[
                    "id",
                    "ville",
                    "pays",
                    "region",
                    "departement",
                    "municipale",
                    "latitude",
                    "longitude",
                    "code_country"
                ]
            )

        print("Recherche de la ville dans la liste...")
        resultat = df[
            df["id"] == value["id"]
        ]


        # Si la ville n'existe pas, je la rajoute dans le FAVOURITE_CITY
        if resultat.empty:
            print("Depuis city favourite cache:" + resultat.columns)

            print("Ville non trouvée dans la liste, ajout en cours...")

            new_row = {
                "id": value["id"],
                "ville": value["city"],
                "pays": value["country"],
                "region": value["region"],
                "departement": value["department"],
                "municipale": value["town"],
                "latitude": value["latitude"],
                "longitude": value["longitude"],
                "code_country": value["code_country"]
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(FAVORITES_CITY, index=False)

            return {
                "erreur": False,
                "message": "Ville ajouté"
            }

        print("Ville trouvée dans la liste : " + resultat["ville"])
        return {
            "erreur": True,
            "message": "Ville déjà existant"
        }

def get_favorite_cities():
    with _lock:
        if FAVORITES_CITY.exists() and FAVORITES_CITY.stat().st_size > 0:
            print("get_favorite_cities: Lecture de la liste des villes en favoris...")
            df = pd.read_csv(FAVORITES_CITY)
            return df[["id", "ville", "pays", "region", "departement", "municipale", "latitude", "longitude", "code_country"]].to_dict('records')
        else:
            print("get_favorite_cities: favorites_city.csv, aucun favoris trouvé...")
            return []

def remove_favorite_cities(id):
    print("remove_favorite_cities : ", id)
    with _lock:
        if FAVORITES_CITY.exists() and FAVORITES_CITY.stat().st_size > 0:
            print("remove_favorite_cities: Lecture de la liste des villes en favoris...")
            df = pd.read_csv(FAVORITES_CITY)

            # Nettoyage et comparaison
            id_a_nettoyer = str(id).strip()
            condition = df["id"].astype(str).str.strip() == id_a_nettoyer

            # Si l'id existe bien dans le BDD
            if condition.any():
                # On garde tout SAUF cette ville
                df_modifie = df[~condition]

                # Sauvegarde dans le fichier CSV
                df_modifie.to_csv(FAVORITES_CITY, index=False)
                print(f"remove_favorite_cities: {id_a_nettoyer} supprimée du CSV.")
                return True
            else:
                print(f"remove_favorite_cities: {id_a_nettoyer} non trouvée dans le CSV.")
                return False
        else:
            print("remove_favorite_cities: favorites_city.csv, aucun favoris trouvé...")
            return False

