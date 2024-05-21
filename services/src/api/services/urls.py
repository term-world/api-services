import sys

from django.urls import path, include

sys.path.insert(0, '../')

import climate_api

climate = climate_api.Climate()

urlpatterns = [
    path('api/v1/climate', climate.get_state),
]
