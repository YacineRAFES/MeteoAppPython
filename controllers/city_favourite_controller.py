from utilitaire.geocoding_cache import get_geocoding


class CityFavouriteController:
    def AddCityFavourite(self, city_name):
        print("Controller : Ajouter une ville favorite : ", city_name)

        # Appel géocoding
        geo = get_geocoding(city_name)
        print(f"Ville ajoutée aux favoris : {geo['ville']} (Code pays : {geo['code_country']}, Latitude : {geo['latitude']}, Longitude : {geo['longitude']})")

        # Ajout de la ville dans la liste des favoris




