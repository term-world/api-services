import json
import requests
import logging
import omnipresence

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin
from .models import Inventory
from .serializers import InventorySerializer
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Set up the logger
logger = logging.getLogger(__name__)

schema_view = get_schema_view(
    openapi.Info(
        title="Inventory API",
        default_version='v1',
        description="API documentation for the Termunda Inventory service.",
        contact=openapi.Contact(email="dluman@allegheny.edu"),
        license=openapi.License(name="CC0"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

class AddInventoryView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            item_owner_record = omnipresence.models.OmnipresenceModel.objects.get(
                charname = request.data.get('item_owner')
            )
            item_owner_id = getattr(item_owner_record, 'id')
            item, created = Inventory.objects.get_or_create(
                item_owner_id = item_owner_id,
                item_name = request.data.get("item_name")
            )
            setattr(item, 'item_bytestring', request.FILES['item_binary'].read())
            if not created: # In the case that the record exists; should be updated
                # Update quantity and space (bulk); TODO: need to figure out how to handle versioning
                qty = getattr(item, 'item_qty') + float(request.data.get('item_qty'))
                setattr(item, 'item_qty', qty)
                # TODO: This is really a trigger?
                setattr(item, 'item_bulk', qty * getattr(item, 'item_weight'))
                # Save modified item to database
                item.save()
            return HttpResponse(
                status = 200
            )
        except Inventory.DoesNotExist:
            serializer = InventorySerializer(data = request.data)
            if not item:
                if serializer.is_valid():
                    serializer.save()
                    return HttpResponse(status=status.HTTP_201_CREATED)
                return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return HttpResponse(status = 400)

class DropInventoryView(APIView):

    # TODO: Potentially also a patch request?

    def post(self, request, *args, **kwargs):
        logger.debug("DropInventoryView POST request data: %s", request.data)
        item_name = request.data.get('item_name')
        item_owner_record = omnipresence.models.OmnipresenceModel.objects.get(
            charname = request.data.get('item_owner')
        )
        if not item_name:
            return Response({"error": "Item name is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not item_owner:
            return HttpResponse({"error": "Item owner ID requred"}, status = 400)
        try:
            inventory_item = Inventory.objects.get(
                item_name = item_name,
                item_owner_id = item_owner
            )
            qty = getattr(inventory_item, 'item_qty')
            setattr(inventory_item, 'item_qty', qty - 1)
            serializer = InventorySerializer(data = inventory_item)
            if serializer.is_valid():
                serializer.save()
            return Response({"message": "Item dropped", "item": inventory_item.as_dict()}, status=status.HTTP_200_OK)
        except Inventory.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

class ListInventoryView(APIView):

    def get(self, request, *args, **kwargs):
        # Retrieve ID of inventory holder
        inventory_owner_data = omnipresence.models.OmnipresenceModel.objects.filter(
            charname = request.GET.get('charname')
        ).values('id')
        # Get information for the inventory holder
        inventory_owner_id = list(inventory_owner_data)[0]['id']
        # Filter inventory based on the inventory holder id
        inventory_items = Inventory.objects.filter(
            item_owner = inventory_owner_id
        )
        # Serialize to re-verify, run other checks
        serializer = InventorySerializer(inventory_items, many=True)
        # Create list representation to transmit back to query
        fields = [obj for obj in serializer.data]
        # Return HTTP response (JSON packet)
        return HttpResponse(
            json.dumps(serializer.data),
            status=status.HTTP_200_OK,
            content_type = 'application/json'
        )

class SearchInventoryView(APIView):

    def post(self, request, *args, **kwargs):
        item_owner_record = omnipresence.models.OmnipresenceModel.objects.get(
            charname = request.data.get('charname')
        )
        item = Inventory.objects.get(
            item_owner_id = getattr(item_owner_record, "id"),
            item_name = request.data.get('item_name')
        )
        response = item.as_dict()
        del response['item_owner']
        response["item_bytestring"] = response['item_bytestring'].hex()
        return HttpResponse(
            json.dumps(response),
            status = 200,
            content_type = 'application/json'
        )
