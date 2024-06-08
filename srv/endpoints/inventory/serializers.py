from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    item_qty = serializers.FloatField(default=1.0)
    item_weight = serializers.FloatField(default=1.0)
    item_bulk = serializers.FloatField(default=1.0)
    item_consumable = serializers.BooleanField(default=False)

    class Meta:
        model = Inventory
        fields = '__all__'

    def validate_item_name(self, value):
        if Inventory.objects.filter(item_name=value).exists():
            raise serializers.ValidationError("An item with this name already exists.")
        return value
