from datetime import datetime

class Conversion:
    @staticmethod
    def from_timestamp_to_datetime(timestamp: int) -> str:
        date = datetime.fromtimestamp(int(timestamp))
        return date.strftime("%A %d %B %Y à %H:%M")

    @staticmethod
    def from_timestamp_to_hour(timestamp: int) -> str:
        hour = datetime.fromtimestamp(int(timestamp))
        return hour.strftime("%H:%M")

    def from_timestamp_to_day(timestamp: int) -> str:
        day = datetime.fromtimestamp(int(timestamp))
        return day.strftime("%A")