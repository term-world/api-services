from rest_framework import serializers
<<<<<<< HEAD:srv/endpoints/api/serializers.py
from .models import Climate


class ClimateSerializer(serializers.ModelSerializer):
    """Serializer for the Climate model."""

    class Meta:
        """Specify the model to be serialized"""

        model = Climate
        fields = ["lat", "lon", "weather_condition"]
=======
from climate.models import TransientModel

class TransientModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransientModel
        fields = ["id"]
>>>>>>> refactor-api-side-branch:srv/endpoints/climate/serializers.py
