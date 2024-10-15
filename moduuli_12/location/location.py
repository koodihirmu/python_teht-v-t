from weather_api.weather_api import WeatherAPI


class Location:
    def __init__(self, city: str) -> None:
        wapi = WeatherAPI()
        self.raw_weather = wapi.getWeather(wapi.getCity(city, 1))
        self.temperature = self.raw_weather["main"]["temp"]
        self.weather = self.raw_weather["weather"][0]["main"]
        self.city = city

    def print_weather(self):
        print(
            f"Weather at {self.city.capitalize()}:\nWeather: {self.weather}\nTemperature (K): {self.temperature}\nTemperature (C): {self.temperature - 273.15:.2f}"
        )
