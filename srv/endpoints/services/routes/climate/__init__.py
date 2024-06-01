import os
import json
import requests

from ..Router import Route

from datetime import datetime
from dotenv import load_dotenv
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

load_dotenv()

try:
    # Retrieve environment variables from .env file
    lat = os.getenv("LAT")
    lon = os.getenv("LON")
    api = os.getenv("OPENWEATHER_API")
    # Make request to OpenWeather API
    print(lat, lon, api)
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"
    )
    STATE = json.loads(data.content)
except Exception as err:
    print(err)
    STATE = {}


class Climate(Route):
    sun = [800, 801]

    def __init__(self):
        super().__init__()
        self.time = datetime.now().timestamp()
        self.windy = self.__is_windy()
        self.sunny = self.__is_sunny() and not self.__is_night()
        self.wind_speed = 0
        if "wind" in STATE:
            self.wind_speed = STATE["wind"]["speed"]

    def __add_url(self, endpoint: str = "", fn: str = "") -> None:
        self.add_url(endpoint, fn)

    def __is_sunny(self) -> bool:
        try:
            for condition in STATE["weather"]:
                if condition["id"] in self.sun:
                    return True
        except:
            pass
        return False

    def __is_night(self) -> bool:
        try:
            sunrise = STATE["sys"]["sunrise"]
            sunset = STATE["sys"]["sunset"]
            if sunrise < self.time < sunset:
                return False
        except:
            return False
        return True

    def __is_windy(self) -> bool:
        try:
            if STATE["wind"]["speed"] > 5:
                return True
        except:
            pass
        return False

    @Route.endpoint("v1")
    def conditions(self, request: WSGIRequest) -> JsonResponse:
        response = {
            "wind": {"windy": self.windy, "windspeed": self.wind_speed},
            "sun": self.sunny,
        }
        return JsonResponse(response, status=200)

    @Route.endpoint("v1")
    def all(self, request: WSGIRequest) -> JsonResponse:
        print(STATE)
        return JsonResponse(STATE, status=200)
