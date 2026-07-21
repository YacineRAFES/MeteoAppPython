import json

from src.resources import resource_path

with resource_path("assets", "weather_code.json").open(encoding="utf-8") as f:
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
            "icon": str(resource_path("assets", weather["image"].split("/")[-1])),
            "description": weather["description"]
        }
