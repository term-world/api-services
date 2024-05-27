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
    if os.path.isdir(f"{route_path}/{entry}"):
        mod_path = route_path.split("/")
        mod = import_module(
            ".".join([*mod_path[-2:], entry]),
            package = entry.capitalize()
        )
        dir(mod)
        #for url in mod.urls:
        #    urlpatterns.append(url)

