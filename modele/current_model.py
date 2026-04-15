from utilitaire.conversion import Conversion
from utilitaire.get_weather_icon import weather_icon


class WeatherCurrent:
    def __init__(self, data):
        self.temperature = data["temperature_2m"]
        self.weather_code = data["weather_code"]
        self.is_day = data["is_day"]
        self.humidity = data["humidity"]
        self.time = data["time"]

    # logique
    def get_temperature(self):
        return round(self.temperature)

    @property
    def get_weather_code(self):
        weather = weather_icon.get_weather_icon(self.weather_code, self.is_day)

        icon = weather["icon"]
        description = weather["description"]

        return icon, description

    def get_humidity(self):
        return self.humidity

    def get_time(self):
        return Conversion.from_timestamp_to_datetime(self.time)