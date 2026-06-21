def parse_current(data):
    current = data["current"]

    return {
        "temperature_2m": current["temperature_2m"],
        "weather_code": current["weather_code"],
        "is_day": current["is_day"],
        "humidity": current["relative_humidity_2m"],
        "time": current["time"]
    }

def parse_hourly(data):
    hourly = data["hourly"]

    return {
        "temperature_2m": hourly["temperature_2m"],
        "weather_code": hourly["weather_code"],
        "is_day": hourly["is_day"],
        "preci_proba": hourly["precipitation_probability"],
        "time": hourly["time"]
    }

def parse_daily(data):
    daily = data["daily"]

    return {
        "temperature_min": daily["temperature_2m_min"],
        "temperature_max": daily["temperature_2m_max"],
        "weather_code": daily["weather_code"],
        "preci_proba": daily["precipitation_probability_max"],
        "time": daily["time"]
    }

def parse_already_current(data):

    return {
        "temperature_2m": data["temperature_2m"],
        "weather_code": data["weather_code"],
        "is_day": data["is_day"],
        "humidity": data["relative_humidity_2m"],
        "time": data["time"]
    }