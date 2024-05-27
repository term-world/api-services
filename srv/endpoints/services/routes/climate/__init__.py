import json
import requests

from ..Router import Route

from datetime import datetime
from django.http import JsonResponse

from django.core.handlers.wsgi import WSGIRequest

try:
    STATE = json.loads(
        requests.get(
            "https://cdn.githubraw.com/term-world/TNN/main/weather.json"
        ).text
    )
except:
    pass

class Climate(Route):

    sun = [800, 801]

    def __init__(self):
        super().__init__()
        self.time = datetime.now().timestamp()
        self.windy = self.__is_windy()
        self.sunny = self.__is_sunny() and not self.__is_night()
        self.wind_speed = STATE["wind"]["speed"]

    def __add_url(self, endpoint: str = "", fn: str = "") -> None:
        self.add_url(endpoint, fn)

    def __is_sunny(self) -> bool:
        for condition in STATE["weather"]:
            if condition["id"] in self.sun:
                return True
        return False

    def __is_night(self) -> bool:
        try:
            sunrise = STATE["sys"]["sunrise"]
            sunset = STATE["sys"]["sunset"]
            if sunrise < self.time < sunset:
                return False
        except KeyError:
            return False
        return True

    def __is_windy(self) -> bool:
        try:
            if STATE["wind"]["speed"] > 5:
                return True
        except KeyError:
            pass
        return False

    @Route.endpoint
    def climate(self, request: WSGIRequest)-> JsonResponse:
        print(self)
        response = {
            "wind": {
                "windy": self.windy,
                "windspeed": self.wind_speed
            },
            "sun": self.sunny
        }
        return JsonResponse(response, status = 200)
