from manager.city_favourite_cache import add_favorite_city, get_favorite_cities, remove_favorite_cities
from manager.geocoding_cache import get_geocoding
from utilitaire.gestion_erreur import gestion_erreur


class CityFavouriteController:
    def AddCityFavourite(self, city_name):
        print("Controller : Ajouter une ville favorite : ", city_name)

        # On verifie si la ville existe dans la liste CSV
        villes_existant = self.GetFavoriteCities()

        if city_name.lower() in [v.lower() for v in villes_existant]:
            return {
                "erreur": True,
                "message": "Ville déjà existant dans la liste CSV"
            }

        # Appel géocoding
        geo = get_geocoding(city_name)
        if not geo:
            print("Controller : Erreur géocoding pour la ville : ", city_name)

        # Ajout de la ville dans la liste des favoris
        result = add_favorite_city(city_name)
        if result:
            return gestion_erreur(False, "La ville a été bien enregistrée.")
        else:
            return gestion_erreur(True, "La ville n'a pas été enregistrée.")

    def GetFavoriteCities(self):
        result = get_favorite_cities()
        if not result:
            print("Controller : Erreur lors de la récupération de la liste des villes favorites")
        return result

    def RemoveCityFavourite(self, object):
        nom_ville = object.text()

        result = remove_favorite_cities(nom_ville)

        if result:
            return gestion_erreur(False, "Suppression d'une ville a été réussie.")
        else:
            return gestion_erreur(True, "Suppression d'une ville n'a pas fonctionné.")
