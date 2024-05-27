import inspect
from typing import Callable
from django.urls import path, include

class Route:

    def __init__(self):
        self.urls = []

    def endpoint(self):
        mod, fn = self.__qualname__.split(".")
        class_name = self.__name__.lower()

    def add_url(self, endpoint: str = "", fn: Callable = callable(None)) -> None:
        if not fn:
            return
        self.urls.append(
            path(endpoint, fn)
        )

