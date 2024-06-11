import sys
import imp
import base64

from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'

    def validate_item_structure(self, item):
        try:
            source = base64.decode(item['item_bytestring'], 'utf8')
            mod = imp.new_module(item['item_name'])
            exec(source, mod.__dict__)
            getattr(mod, item['item_name'])().use
        except:
            # TODO: Raise individual exceptions for parts of the flow above?
            raise serializers.ValidationError(
                {"item_binary": "Item binary does not represent a valid item."}
            )
        return binary
