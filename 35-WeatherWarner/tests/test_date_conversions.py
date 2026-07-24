from datetime import datetime

from weather_warner.date_conversions import to_iso_datetime

def test_to_iso_datetime():
    dt = to_iso_datetime(datetime(2024, 6, 1, 12, 30, 45))
    assert dt == "2024-06-01 12:30:45"
