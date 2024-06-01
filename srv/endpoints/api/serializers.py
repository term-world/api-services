from rest_framework import serializers
from .models import Climate


class ClimateSerializer(serializers.ModelSerializer):
    """Serializer for the Climate model."""

    class Meta:
        """Specify the model to be serialized"""

        model = Climate
        fields = ["lat", "lon", "weather_condition"]
