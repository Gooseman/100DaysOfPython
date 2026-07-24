from weather_warner.date_conversions import epoch_to_datetime, to_iso_datetime
from weather_warner.open_weather_urls import BASE_FORECAST_URL
from weather_warner.requester import get_request
from weather_warner.weather import Weather

THREE_HOURS = 3 * 60 * 60

def get_hourly_weather_data(lat, long, api_key) -> Weather:
    base_url = BASE_FORECAST_URL
    params = {
        "lat": lat,
        "lon": long,
        "appid": api_key,
        # Number of 3 hour intervals to retrieve (8 intervals = 24 hours)
        "cnt": 8,
        # Use metric units (Celsius)
        "units": "metric",
    }
    response = get_request(base_url, params=params)

    return parse_weather_data(response)

def parse_weather_data(weather_data) -> Weather:
    """
    Parses the weather data to find min and max temperatures, when rain is expected, wind, sunrise and sunset.

    Args:
        weather_data (dict): The weather data returned from the OpenWeatherMap API.

    Returns:
        Weather: An instance of the Weather class containing the relevant weather information.
    """
    city_data = weather_data.get("city", {})
    weather = Weather(_get_city_name(city_data))
    sunrise, sunset = _get_sunrise_sunset(city_data)
    min_temp = 1000
    max_temp = -1000

    weather.set_sunrise(sunrise).set_sunset(sunset)

    for entry in weather_data.get("list", []):
        epoch_time = entry.get("dt")
        entry_time = to_iso_datetime(epoch_to_datetime(epoch_time))
        main_data = entry.get("main", {})
        wind_data = entry.get("wind", {})
        temp_feel = main_data.get("feels_like")

        min_temp = min(min_temp, temp_feel)
        max_temp = max(max_temp, temp_feel)

        weather.add_temperature(
            time=entry_time,
            temp=main_data.get("temp"),
            feels_like=temp_feel
        )
        weather.add_wind(
            time=entry_time,
            speed=wind_data.get("speed"),
            direction=wind_data.get("deg")
        )

        if "rain" in entry:
            weather.add_rain(
                # The rain volume is for the previous 3 hours, not the next 3 hours
                time=to_iso_datetime(epoch_to_datetime(epoch_time - THREE_HOURS)),
                amount=entry.get("rain", {}).get("3h", 0)
            )

    weather.set_temp_range(min_temp, max_temp)
    return weather

def _get_city_name(city_data):
    """
    Extracts the city name from the weather data.

    Args:
        city_data (dict): The city data extracted from the weather data.

    Returns:
        str: The name of the city.
    """
    return f"{city_data.get('name', '')}, {city_data.get('country', '')}"

def _get_sunrise_sunset(city_data):
    """
    Extracts the sunrise and sunset times from the city data.

    Args:
        city_data (dict): The city data extracted from the weather data.

    Returns:
        tuple: A tuple containing the sunrise and sunset times as strings.
    """
    sunrise = to_iso_datetime(epoch_to_datetime(city_data.get("sunrise")))
    sunset = to_iso_datetime(epoch_to_datetime(city_data.get("sunset")))

    return sunrise, sunset
