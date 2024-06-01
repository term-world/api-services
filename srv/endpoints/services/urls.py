import os
from importlib import import_module

from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .viewsets import ClimateViewSet
from rest_framework.schemas import get_schema_view

route_path = "services/routes"
urlpatterns = []

for entry in os.listdir(route_path):
    if os.path.isdir(f"{route_path}/{entry}") and entry != "__pycache__":
        mod_path = route_path.split("/")
        mod = import_module(
            ".".join([*mod_path[-2:], entry]), package=entry.capitalize()
        )

        cls = mod.__dict__[entry.capitalize()]
        for method in dir(cls):
            elem = getattr(cls, method)
            if "decorated" in dir(elem):
                instance = cls()
                urlpatterns.append(
                    path(
                        f"{elem.version}/{elem.endpoint}/{elem.__name__}",
                        getattr(instance, elem.__name__),
                    )
                )

# Create a default router and register the ClimateViewSet
router = DefaultRouter()
router.register(r"climate", ClimateViewSet)

# Define the urlpatterns, including the routes for the router and the schema view
urlpatterns = [
    path("", include(router.urls)),
    path("docs/", get_schema_view(title="Climate API Documentation")),
    # Other urls...
]
