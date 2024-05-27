import os
import sys
import pennant
from importlib import import_module

from django.urls import path, include

route_path = 'services/routes'
urlpatterns = []

for entry in os.listdir(route_path):
    if os.path.isdir(f"{route_path}/{entry}") and entry != "__pycache__":
        mod_path = route_path.split("/")
        mod = import_module(
            ".".join([*mod_path[-2:], entry]),
            package = entry.capitalize()
        )

        cls = mod.__dict__[entry.capitalize()]
        for method in dir(cls):
            elem = getattr(cls, method)
            if 'decorated' in dir(elem):
                instance = cls()
                urlpatterns.append(
                    path(
                        f"{elem.version}/{elem.endpoint}/{elem.__name__}",
                        getattr(instance, elem.__name__)
                    )
                )
