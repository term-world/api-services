from django.db import models


# Create your models here.
class Climate(models.Model):
    """Climate model that represents climate data for a specific location."""

    lat = models.FloatField()
    lon = models.FloatField()
    weather_condition = models.IntegerField()
