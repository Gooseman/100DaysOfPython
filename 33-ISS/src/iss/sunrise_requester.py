import requests

# SUNRISE_URL = "https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0"
SUNRISE_URL = "https://api.sunrise-sunset.org/json"

def _parse_sunrise_sunset(data):
    """Get the sunrise and sunset times from the API response data."""
    try:
        sunrise = data["sunrise"]
        sunset = data["sunset"]
        return sunrise, sunset
    except KeyError as e:
        print(f"Key error while parsing sunrise/sunset data: {e}")
        return None
    
def get_sunrise_sunset(latitude, longitude):
    """
    Get the sunrise and sunset times for a given latitude and longitude.

    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.
    Returns:
        dict: A dictionary containing the sunrise and sunset times in ISO 8601 format.
    """
    parameters = {
        "lat": latitude,
        "lng": longitude,
        "formatted": 0
    }
    # url = SUNRISE_URL.format(latitude=latitude, longitude=longitude)
    
    try:
    # response = requests.get(url, timeout=30)
        response = requests.get(SUNRISE_URL, params=parameters, timeout=30)

        response.raise_for_status()

        data = response.json()

        return _parse_sunrise_sunset(data["results"])
    except requests.exceptions.Timeout as e:
        print(f"Request timed out while fetching sunset for location ({latitude}, {longitude}): {e}")
        return None
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error occurred while fetching sunset for location ({latitude}, {longitude}): {e}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred while fetching sunset for location ({latitude}, {longitude}): {e}")
        return None
    except requests.RequestException as e:
        print(f"An error occurred while fetching sunset for location ({latitude}, {longitude}): {e}")
        return None