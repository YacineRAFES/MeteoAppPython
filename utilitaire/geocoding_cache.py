from string import capwords
import pandas as pd
from pathlib import Path

from services.geo.geocoding import get_geo

CACHE_PATH = Path(__file__).parent.parent / "cache" / "geocoding.csv"

def get_geocoding(nomville):

    # Je vérifie si la ville existe dans le geocoding cache
    if CACHE_PATH.exists() and CACHE_PATH.stat().st_size > 0:
        print("Lecture du cache de géocodage...")
        df = pd.read_csv(CACHE_PATH)
    else:
        print("Cache de géocodage vide ou inexistant, création d'un nouveau cache...")
        df = pd.DataFrame(columns=["ville", "code_country", "latitude", "longitude"])

    print("Recherche de la ville dans le cache..." + nomville)
    result = df[df["ville"] == capwords(nomville)]


    # Si la ville n'existe pas, je la rajoute dans le cache
    if result.empty:
        print("Ville non trouvée dans le cache, ajout en cours..." + nomville)
        geo = GeoCoding()
        geocoding = geo.GetGeo(nomville)
        new_row = {
            "ville": capwords(nomville),
            "code_country": geocoding["code_country"],
            "latitude": geocoding["latitude"],
            "longitude": geocoding["longitude"]
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(CACHE_PATH, index=False)
        return new_row

    print("Ville trouvée dans le cache : " + nomville)
    return result.iloc[0].to_dict()