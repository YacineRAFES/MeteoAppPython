from pathlib import Path

import pandas as pd

from modele.current_model import WeatherCurrent
from services.geo.geocoding import get_geo
from services.weather.weather_parser import parse_current


class InternationalController:


    def __init__(self):
        super().__init__()
        self.INTERNATIONAL_FILE = None

