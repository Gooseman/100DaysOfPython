

class Rain:
    def __init__(self, time: str, amount: float):
        self.time = time
        self.amount = amount

class Wind:
    def __init__(self, time: str, speed: float, direction: str):
        self.time = time
        self.speed = speed
        self.direction = direction

class Temperature:
    def __init__(self, time: str, temp: float, feels_like: float):
        self.time = time
        self.temp = temp
        self.feels_like = feels_like

class Weather:
    def __init__(self, city: str):
        self._city = city
        self._sunrise = 0
        self._sunset = 0
        self._rain_expected: list[Rain] = []
        self._wind: list[Wind] = []
        self._temperature: list[Temperature] = []
        self._min_temp = 0
        self._max_temp = 0

    def set_sunrise(self, sunrise: str) -> Weather:
        self._sunrise = sunrise
        return self

    def set_sunset(self, sunset: str) -> Weather:
        self._sunset = sunset
        return self

    def add_rain(self, time: str, amount: float) -> Weather:
        self._rain_expected.append(Rain(time, amount))
        return self

    def add_wind(self, time: str, speed: float, direction: str) -> Weather:
        self._wind.append(Wind(time, speed, direction))
        return self

    def add_temperature(self, time: str, temp: float, feels_like: float) -> Weather:
        self._temperature.append(Temperature(time, temp, feels_like))
        return self

    def set_temp_range(self, min_temp: float, max_temp: float) -> Weather:
        self._min_temp = min_temp
        self._max_temp = max_temp
        return self

    def to_dict(self) -> dict:
        return {
            "city": self._city,
            "sunrise": self._sunrise,
            "sunset": self._sunset,
            "min_temp": self._min_temp,
            "max_temp": self._max_temp,
            # "temperature": [vars(temp) for temp in self._temperature],
            "rain_expected": [vars(rain) for rain in self._rain_expected],
            # "wind": [vars(wind) for wind in self._wind]
        }

    def to_str(self) -> str:
        return f"Weather\n" \
               f"City: {self._city},\n" \
               f"Sunrise: {self._sunrise},\n" \
               f"Sunset: {self._sunset},\n" \
               f"Min (feels like): {self._min_temp},\n" \
               f"Max (feels like): {self._max_temp}\n" \
               f"{self._rain_to_str()}"

    def _rain_to_str(self) -> str:
        rain_str = "Rain:\n"

        if not self._rain_expected:
            return rain_str + "  No rain expected.\n"

        for rain in self._rain_expected:
            rain_str += f"  Time: {rain.time}, Amount: {rain.amount}\n"

        return rain_str
