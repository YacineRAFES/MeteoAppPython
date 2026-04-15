from utilitaire.conversion import Conversion
from utilitaire.get_weather_icon import weather_icon


class WeatherDaily:
    def __init__(self, data):
        self.temp_min = data["temperature_min"]
        self.temp_max = data["temperature_max"]
        self.weather_code = data["weather_code"]
        self.precipitations = data["preci_proba"]
        self.times = data["time"]

    def get_temp_min(self, index):
        return self.temp_min[index]

    def get_temp_max(self, index):
        return self.temp_max[index]

    @property
    def get_weather_code(self):
        weather = weather_icon.get_weather_icon(self.weather_code, 1)

        icon = weather["icon"]
        description = weather["description"]

        return icon, description

    def get_precipitations(self, index):
        return self.precipitations[index]

    def get_times(self, index):
        return Conversion.from_timestamp_to_day(self.times[index])