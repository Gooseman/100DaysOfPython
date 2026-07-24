from weather_warner.requester import get_request

from weather_warner.open_weather_urls import GEOLOCATION_URL

class CityRetriever:
    def __init__(self, api_key):
        self.api_key = api_key
        self.known_cities = {}

    def get_city_coordinates(self, city_name, api_key):
        """
        Fetches the geographical coordinates (latitude and longitude) of a city using the OpenWeatherMap API.

        Args:
            city_name (str): The name of the city to fetch coordinates for.  This can include the country code and, if 
                            necessary, the state (e.g., "London,GB" or "London,CA,US").
            api_key (str): Your OpenWeatherMap API key.

        Returns:
            dict: A dictionary containing the latitude and longitude of the city, or an empty dictionary if the request 
                    fails.
        """
        if city_name in self.known_cities:
            return self.known_cities[city_name]

        geo_url = f"{GEOLOCATION_URL}/direct"
        params = {"q": city_name, "appid": api_key}
        response = get_request(geo_url, params=params)

        if response:
            coords = { "lat": response[0]["lat"], "lon": response[0]["lon"] }

            self.known_cities[city_name] = coords
            return coords

        return {}
