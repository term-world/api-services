import os
import requests
from collections import UserList
from django.db import models
from django.core.cache import caches
from dotenv import load_dotenv

load_dotenv()
CACHE = caches["default"]

# This functionality builds on an answer for the following SO question,
# but not the accepted answer; this one is farther down in the post:
#
# https://stackoverflow.com/questions/9091305/django-models-without-database


class TransientModelManager(models.Manager):

    api = os.getenv("OPENWEATHER_API")
    lat = os.getenv("OPENWEATHER_LAT")
    lon = os.getenv("OPENWEATHER_LON")

    cache_key = "cached-transient-models"
    cache_sentinel = object()
    cache_timeout = 600

    def get_queryset(self):
        transient_model_data = CACHE.get(self.cache_key, self.cache_sentinel)
        if transient_model_data is self.cache_sentinel:
            response = requests.get(
                 f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.api}"
            )
            response.raise_for_status()
            transient_model_data = response.json()
            CACHE.set(self.cache_key, transient_model_data, self.cache_timeout)
        return TransientModelQueryset([
            TransientModel(*data)
            for data in transient_model_data
        ])

class TransientModelQueryset(UserList):
    pass

class TransientModel(models.Model):
    class Meta:
        managed = False

    obj = TransientModelManager.from_queryset(TransientModelQueryset)()
