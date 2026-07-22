from src.manager.city_favourite_cache import add_favorite_city, get_favorite_cities, remove_favorite_cities
from src.services.geo.geocoding import get_geocoding
from src.utilitaire.gestion_erreur import gestion_erreur


class CityFavouriteController:
    def AddCityFavourite(self, value, action):
        if action == "Search":
            print("Controller : Search : " + value)

            # On envoie une requête geocoding

            geo = get_geocoding(value)
            if not geo:
                print("probleme de geocoding")
                return {
                    "erreur": True,
                    "message": "Probleme de geocoding"
                }

            else:
                print("requete geocoding recu")
                return {
                    "erreur": False,
                    "data": geo
                }
        elif action == "Add":
            print("Controller : Ajouter une ville favorite !")
            result = add_favorite_city(value)

            if result["erreur"]:
                return {
                    "erreur": True,
                    "message": result["message"]
                }
            else:
                return {
                    "erreur": False,
                    "data": result["message"]
                }

    def GetFavoriteCities(self):
        result = get_favorite_cities()
        if not result:
            print("Controller : Erreur lors de la récupération de la liste des villes favorites")
        return result

    def RemoveCityFavourite(self, id):

        result = remove_favorite_cities(id)

        if result:
            return gestion_erreur(False, "Suppression d'une ville a été réussie.")
        else:
            return gestion_erreur(True, "Suppression d'une ville n'a pas fonctionné.")
