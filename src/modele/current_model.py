from src.utilitaire.conversion import Conversion
from src.utilitaire.get_weather_icon import weather_icon


class WeatherCurrent:
    def __init__(self, data):
        self.temperature_2m = data["temperature_2m"]
        self.weather_code = data["weather_code"]
        self.is_day = data["is_day"]
        self.relative_humidity_2m = data["relative_humidity_2m"]
        self.time = data["time"]
        self.code_country = None
        self.city = None

    # logique
    def get_temperature_2m(self):
        return round(self.temperature_2m)

    @property
    def get_weather_code(self):
        weather = weather_icon.get_weather_icon(self.weather_code, self.is_day)

        icon = weather["icon"]
        description = weather["description"]

        return icon, description

    def get_relative_humidity_2m(self):
        return self.relative_humidity_2m

    def get_time(self):
        return Conversion.from_timestamp_to_datetime(self.time)