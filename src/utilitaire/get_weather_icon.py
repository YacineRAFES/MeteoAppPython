import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "assets", "weather_code.json")) as f:
    WEATHER_DATA = json.load(f)

class weather_icon:
    @staticmethod
    def get_weather_icon(weather_code, is_day):
        if is_day:
            period = "day"
        else:
            period = "night"
        weather = WEATHER_DATA[str(weather_code)][period]

        return {
            "icon": os.path.join(BASE_DIR, "assets", os.path.basename(weather['image'])),
            "description": weather["description"]
        }
