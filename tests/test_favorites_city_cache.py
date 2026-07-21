from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

from src.manager import city_favourite_cache


class TestFavoritesCityCache(TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.cache_path = Path(self.temp_dir.name) / "favorites_city.csv"
        self.city = {
            "id": 1,
            "city": "Paris",
            "country": "France",
            "region": "Ile-de-France",
            "department": "Paris",
            "town": "Paris",
            "latitude": 48.8566,
            "longitude": 2.3522,
            "code_country": "FR",
        }

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_get_and_remove_favorite_city(self):
        with patch.object(city_favourite_cache, "FAVORITES_CITY", self.cache_path):
            self.assertFalse(city_favourite_cache.add_favorite_city(self.city)["erreur"])
            self.assertTrue(city_favourite_cache.add_favorite_city(self.city)["erreur"])

            favorites = city_favourite_cache.get_favorite_cities()
            self.assertEqual(favorites[0]["ville"], "Paris")

            self.assertTrue(city_favourite_cache.remove_favorite_cities(1))
            self.assertEqual(city_favourite_cache.get_favorite_cities(), [])
