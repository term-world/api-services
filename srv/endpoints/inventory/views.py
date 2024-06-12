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
            item, created = Inventory.objects.get_or_create(
                item_owner_id = request.data.get("item_owner"),
                item_name = request.data.get("item_name")
            )
            # Update quantity; TODO: need to figure out how to handle versioning
            qty = getattr(item, 'item_qty') + float(request.data.get('item_qty'))
            setattr(item, 'item_qty', qty)
            setattr(item, 'item_bulk', qty * getattr(item, 'item_weight'))
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

class DropInventoryView(APIView):

    # TODO: Potentially also a patch request?

    def post(self, request, *args, **kwargs):
        logger.debug("DropInventoryView POST request data: %s", request.data)
        item_name = request.data.get('item_name')
        if not item_name:
            return Response({"error": "Item name is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            inventory_item = Inventory.objects.get(item_name=item_name)
            inventory_item.delete()
            return Response({"message": "Item dropped"}, status=status.HTTP_200_OK)
        except Inventory.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

class UpdateInventoryView(GenericAPIView, UpdateModelMixin):

    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def patch(self, request, *args, **kwargs):
        if not request.data.get('item_name'):
            return HttpResponse(
                json.dumps({"error": "Item name required."}),
                status = 400,
                content_type = "application/json"
            )
        return self.partial_update(request, *args, **kwargs)

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
