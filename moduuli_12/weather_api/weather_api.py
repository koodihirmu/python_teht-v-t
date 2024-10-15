import json

import requests

# https://openweathermap.org/api/geocoding-api
# https://openweathermap.org/api/one-call-3


class WeatherAPI:
    def __init__(self) -> None:
        if __debug__:
            print("Initializing WeatherAPI")
            # getting secrets from a json in project root
        with open("secret.json") as file:
            json_file = json.load(file)
            self.api_key = json_file["weather_api"]["api_key"]

    def getCity(self, city_name: str, limit: int) -> tuple[float, float]:
        request = f"""https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={self.api_key}"""
        response = requests.get(request)
        response.raise_for_status()
        json_response = response.json()
        return (json_response[0]["lat"], json_response[0]["lon"])

    def getWeather(self, coordinates: tuple[float, float]) -> dict:
        request = f"""https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0]}&lon={coordinates[1]}&appid={self.api_key}"""
        response = requests.get(request)
        response.raise_for_status()
        json_response = response.json()
        return json_response


if __name__ == "__main__":
    try:
        wapi = WeatherAPI()
        print(wapi.getWeather(wapi.getCity("porvoo", 1)))
    except Exception as e:
        print(e)
    input("Press Enter ...")
