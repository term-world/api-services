from rest_framework import serializers
from climate.models import ClimateModel

class ClimateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimateModel
        fields = [
            "coord",
            "weather",
            "base",
            "main",
            "visibility",
            "wind",
            "clouds",
            "dt",
            "sys",
            "timezone",
            "id",
            "name",
            "cod"
        ]
