import os

from weather_warner.city_retriever import CityRetriever
from weather_warner.telegram import send_telegram_message
from weather_warner.weather_retriever import get_hourly_weather_data

APP_ID = os.getenv("OPENWEATHERMAP_APP_ID")

if __name__ == "__main__":
    print(APP_ID)
    city_retriever = CityRetriever(APP_ID)

    location = city_retriever.get_city_coordinates("London,GB", APP_ID)
    weather = get_hourly_weather_data(location["lat"], location["lon"], APP_ID)

    print(location)
    print(weather.to_str())
    send_telegram_message(weather.to_str())
