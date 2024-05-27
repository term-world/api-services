import os
import sys
import pennant
from importlib import import_module

from django.urls import path, include

# TODO: Transition to a plugin-like approach that inherits
#       urls.py files from the individual services?

route_path = 'services/routes'
urlpatterns = []

for entry in os.listdir(route_path):
    if os.path.isdir(f"{route_path}/{entry}") and entry != "__pycache__":
        mod_path = route_path.split("/")
        mod = import_module(
            ".".join([*mod_path[-2:], entry]),
            package = entry.capitalize()
        )

        # TODO: Make the search case insensitive? Still need to enforce
        #       naming structure

        cls = mod.__dict__[entry.capitalize()]
        for method in dir(cls):
            elem = getattr(cls, method)
            if 'decorated' in dir(elem):
                instance = cls()
                urlpatterns.append(
                    path(
                        f"{elem.version}/{elem.__name__}",
                        getattr(instance, elem.__name__)
                    )
                )
                print(f"LIST: {elem.version}/{elem.__name__} @ {cls}")
