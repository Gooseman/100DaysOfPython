import requests

LOCATION_URL = "http://api.open-notify.org/iss-now.json"

def parse_iss_location(data):
    try:
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]
        return latitude, longitude
    except KeyError as e:
        print(f"Key error while parsing ISS location: {e}")
        return None

def get_iss_location():
    try:
        response = requests.get(LOCATION_URL, timeout=30)

        if 300 > response.status_code >= 200:
            data = response.json()

            return parse_iss_location(data)

        print(f"Failed to fetch ISS location. Status code: {response.status_code} ({response.reason})")
        return float("nan"), float("nan")
    except requests.exceptions.Timeout as e:
        print(f"Request timed out while fetching ISS location: {e}")
        return None
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error occurred while fetching ISS location: {e}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred while fetching ISS location: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching ISS location: {e}")
        return None
