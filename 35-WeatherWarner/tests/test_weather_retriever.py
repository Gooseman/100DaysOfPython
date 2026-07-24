from weather_warner import weather_retriever
from weather_warner.date_conversions import epoch_to_datetime, to_iso_datetime


# pylint: disable=too-many-arguments
def make_entry(dt, temp, feels_like, wind_speed=1.0, wind_deg=0, rain=None):
    entry = {
        "dt": dt,
        "main": {"temp": temp, "feels_like": feels_like},
        "wind": {"speed": wind_speed, "deg": wind_deg}
    }
    if rain is not None:
        entry["rain"] = {"3h": rain}
    return entry

ONE_HOUR = 60 * 60
CITY = "TestCity"
COUNTRY = "TC"

def test_parse_weather_data_with_rain():
    sunrise = 1620000000
    sunset = 1620040000
    min_temp = 8.0
    min_feels_like = 7.0
    max_temp = 12.0
    max_feels_like = 11.0
    rain_amount = 2.5
    entries = [
        make_entry(sunrise + ONE_HOUR, (min_temp + max_temp) / 2, (min_feels_like + max_feels_like) / 2),
        make_entry(sunrise + 2 * ONE_HOUR, min_temp, min_feels_like, rain=rain_amount),
        make_entry(sunrise + 3 * ONE_HOUR, max_temp, max_feels_like),
    ]

    weather_data = {
        "city": {"name": CITY, "country": COUNTRY, "sunrise": sunrise, "sunset": sunset},
        "list": entries,
    }

    weather = weather_retriever.parse_weather_data(weather_data)
    d = weather.to_dict()

    assert d["city"] == f"{CITY}, {COUNTRY}"
    assert d["min_temp"] == min_feels_like
    assert d["max_temp"] == max_feels_like

    # One rain entry expected
    assert len(d["rain_expected"]) == 1
    rain = d["rain_expected"][0]

    # Rain time should be dt - 3 hours, converted to ISO
    expected_rain_time = to_iso_datetime(epoch_to_datetime(1620007200 - 3 * 60 * 60))
    assert rain["amount"] == 2.5
    assert rain["time"] == expected_rain_time


def test_parse_weather_data_without_rain():
    sunrise = 1620000000
    sunset = 1620040000
    min_temp = 5.0
    min_feels_like = 4.0
    max_temp = 7.5
    max_feels_like = 7.0
    entries = [
        make_entry(sunrise + ONE_HOUR, min_temp, min_feels_like),
        make_entry(sunrise + 2 * ONE_HOUR, max_temp, max_feels_like),
        make_entry(sunrise + 3 * ONE_HOUR, (min_temp + max_temp) / 2, (min_feels_like + max_feels_like) / 2),
    ]

    weather_data = {
        "city": {"name": CITY, "country": COUNTRY, "sunrise": sunrise, "sunset": sunset},
        "list": entries,
    }

    weather = weather_retriever.parse_weather_data(weather_data)
    weather_report = weather.to_dict()

    assert weather_report["city"] == f"{CITY}, {COUNTRY}"
    assert weather_report["min_temp"] == min_feels_like
    assert weather_report["max_temp"] == max_feels_like
    assert weather_report["rain_expected"] == []
