from utilitaire.conversion import Conversion
from utilitaire.get_weather_icon import weather_icon


class WeatherHourly:
    def __init__(self, data):
        self.temperature_2m = data["temperature_2m"]
        self.weather_code = data["weather_code"]
        self.is_day = data["is_day"]
        self.precipitation_probability = data["precipitation_probability"]
        self.times = data["time"]
        self.precipitation = data["precipitation"]

    def get_temperature_2m(self, index):
        return round(self.temperature_2m[index])

    def get_weather_code(self, index):
        weather = weather_icon.get_weather_icon(self.weather_code[index], self.is_day[index])

        icon = weather["icon"]
        description = weather["description"]

        return icon, description

    def get_precipitation_probability(self, index):
        return self.precipitation_probability[index]

    def get_times(self, index):
        return Conversion.from_timestamp_to_hour(self.times[index])

    def get_precipitation(self, index):
        return self.precipitation[index]

    def get_all_temperatures(self):
        return [self.get_temperature_2m(i) for i in range(len(self.temperature_2m))]

    def get_all_times(self):
        return [self.get_times(i) for i in range(len(self.times))]

    def get_all_precipitations(self):
        return [self.get_precipitation(i) for i in range(len(self.precipitation))]