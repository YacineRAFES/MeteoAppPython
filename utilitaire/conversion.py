from datetime import datetime

class Conversion:
    @staticmethod
    def from_timestamp_to_datetime(timestamp: int) -> str:
        date = datetime.fromtimestamp(int(timestamp))
        return date.strftime("%A %d %B %Y à %H:%M")
