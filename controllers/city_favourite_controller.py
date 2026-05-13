from utilitaire.city_favourite_cache import add_city_favourite, get_favorite_cities
from utilitaire.geocoding_cache import get_geocoding


class CityFavouriteController:
    def AddCityFavourite(self, city_name):
        print("Controller : Ajouter une ville favorite : ", city_name)

        # Appel géocoding
        geo = get_geocoding(city_name)
        if not geo:
            print("Controller : Erreur géocoding pour la ville : ", city_name)

        # Ajout de la ville dans la liste des favoris
        result = add_city_favourite(city_name)
        if not result:
            print("Controller : Erreur lors de l'ajout de la ville dans les favoris : ", city_name)

        # Appel pour refresh la liste des villes favorites
        self.GetFavoriteCities()

    def GetFavoriteCities(self):
        result = get_favorite_cities()
        if not result:
            print("Controller : Erreur lors de la récupération de la liste des villes favorites")
        return result




