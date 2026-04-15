from unittest import TestCase

from modele.current_model import WeatherCurrent


class TestWeatherCurrent(TestCase):
    def setUp(self):
        self.data = {
            "temperature_2m": 20.6,
            "weather_code": 1,
            "is_day": 1,
            "humidity": 50,
            "time": 1776266616
        }
        self.current = WeatherCurrent(self.data)

    def test_get_temperature_arrondi(self):
        self.assertEqual(self.current.get_temperature(), 21, "Température arrondie devrait être 21")

    def test_get_weather_code(self):
        icon, desc = self.current.get_weather_code

        self.assertIsInstance(icon, str)
        self.assertIsInstance(desc, str)

    def test_get_humidity(self):
        self.assertEqual(self.current.get_humidity(), 50, "Humidité devrait être 50")

    def test_get_time(self):
        result = self.current.get_time()

        self.assertIsInstance(result, str)
        self.assertIn("2026", result)