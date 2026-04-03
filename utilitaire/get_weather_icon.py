import json

with open("./assets/weather_code.json") as f:
    WEATHER_DATA = json.load(f)

class weather_icon:
    def get_weather_icon(self, weather_code, is_day):
        period = "day" if is_day else "night"
        weather = WEATHER_DATA[str(weather_code)][period]
        print(f"Code météo: {weather_code}, Période: {period}, Icon: {weather['image']}, Description: {weather['description']}")

        return {
            "icon": weather['image'],
            "description": weather["description"]
        }
