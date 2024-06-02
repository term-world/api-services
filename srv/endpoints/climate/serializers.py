from rest_framework import serializers
from climate.models import TransientModel

class TransientModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransientModel
