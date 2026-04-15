from utilitaire.conversion import Conversion
from utilitaire.get_weather_icon import weather_icon


class WeatherHourly:
    def __init__(self, data):
        self.temperatures = data["temperature_2m"]
        self.weather_code = data["weather_code"]
        self.is_day = data["is_day"]
        self.precipitations = data["preci_proba"]
        self.times = data["time"]

    def get_temperatures(self, index):
        return self.temperatures[index]

    def get_weather_code(self, index):
        weather = weather_icon.get_weather_icon(self.weather_code[index], self.is_day[index])

        icon = weather["icon"]
        description = weather["description"]

        return icon, description

    def get_precipitations(self, index):
        return self.precipitations[index]

    def get_times(self, index):
        return Conversion.from_timestamp_to_hour(self.times[index])