def parse_current(data):
    current = data["current"]

    return {
        "temperature_2m": current["temperature_2m"],
        "weather_code": current["weather_code"],
        "is_day": current["is_day"],
        "relative_humidity_2m": current["relative_humidity_2m"],
        "time": current["time"]
    }

def parse_hourly(data):
    hourly = data["hourly"]

    return {
        "temperature_2m": hourly["temperature_2m"],
        "weather_code": hourly["weather_code"],
        "is_day": hourly["is_day"],
        "precipitation_probability": hourly["precipitation_probability"],
        "time": hourly["time"],
        "precipitation": hourly["precipitation"]
    }

def parse_daily(data):
    daily = data["daily"]

    return {
        "temperature_2m_min": daily["temperature_2m_min"],
        "temperature_2m_max": daily["temperature_2m_max"],
        "weather_code": daily["weather_code"],
        "precipitation_probability_max": daily["precipitation_probability_max"],
        "time": daily["time"]
    }

def parse_already_current(data):

    return {
        "temperature_2m": data["temperature_2m"],
        "weather_code": data["weather_code"],
        "is_day": data["is_day"],
        "relative_humidity_2m": data["relative_humidity_2m"],
        "time": data["time"]
    }