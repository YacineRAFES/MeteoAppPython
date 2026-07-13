from utilitaire.conversion import Conversion
from utilitaire.get_weather_icon import weather_icon


class WeatherDaily:
    def __init__(self, data):
        self.temperature_2m_min = data["temperature_2m_min"]
        self.temperature_2m_max = data["temperature_2m_max"]
        self.weather_code = data["weather_code"]
        self.precipitation_probability_max = data["precipitation_probability_max"]
        self.day = data["time"]

    def get_temperature_2m_min(self, index):
        return round(self.temperature_2m_min[index])

    def get_temperature_2m_max(self, index):
        return round(self.temperature_2m_max[index])

    def get_weather_code(self, index):
        weather = weather_icon.get_weather_icon(self.weather_code[index], 1)

        icon = weather["icon"]
        description = weather["description"]

        return icon, description

    def get_precipitation_probability_max(self, index):
        return self.precipitation_probability_max[index]

    def get_day(self, index):
        return Conversion.from_timestamp_to_day(self.day[index])