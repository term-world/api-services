# import sys

# from django.urls import path, include

# sys.path.insert(0, '../')

# import climate_api

# climate = climate_api.Climate()

# urlpatterns = [
#     path('api/v1/climate', climate.call),
# ]

from django.urls import path
from .views import inventory_view

urlpatterns = [
    path('inventory/', inventory_view, name='inventory_view'),
]


