import sys

from django.urls import path, include

sys.path.insert(0, '../')

import climate_api

urlpatterns = [
    path('api/v1/climate', climate_api.Climate().get_state),
]
