import json
import requests

from datetime import datetime
from django.http import JsonResponse

from django.core.handlers.wsgi import WSGIRequest

STATE = json.loads(
    requests.get(
        "https://cdn.githubraw.com/term-world/TNN/main/weather.json"
    ).text
)

class Climate:

    sun = [800, 801]

    def __init__(self):
        self.time = datetime.now().timestamp()
        self.windy = self.__is_windy()
        self.sunny = self.__is_sunny() and not self.__is_night()
        self.wind_speed = STATE["wind"]["speed"]

    def __is_sunny(self) -> bool:
        for condition in STATE["weather"]:
            if condition["id"] in self.sun:
                return True
        return False

    def __is_night(self) -> bool:
        sunrise = STATE["sys"]["sunrise"]
        sunset = STATE["sys"]["sunset"]
        if sunrise < self.time < sunset:
            return False
        return True

    def __is_windy(self) -> bool:
        if STATE["wind"]["speed"] > 5:
            return True
        return False

    def call(self, request: WSGIRequest)-> JsonResponse:
        response = {
            "wind": {
                "windy": self.windy,
                "windspeed": self.wind_speed
            },
            "sun": self.sunny
        }
        return JsonResponse(response, status = 200)
