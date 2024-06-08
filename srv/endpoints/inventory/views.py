from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory
from .serializers import InventorySerializer
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
import logging

# Set up the logger
logger = logging.getLogger(__name__)

schema_view = get_schema_view(
    openapi.Info(
        title="Inventory API",
        default_version='v1',
        description="API documentation for the Inventory app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@inventory.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

class AddInventoryView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        # Set default values
        data.setdefault('item_weight', 1.0)
        data.setdefault('item_bulk', 1.0)
        data.setdefault('item_consumable', False)
        serializer = InventorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DropInventoryView(APIView):
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

class UpdateInventoryView(APIView):
    def post(self, request, *args, **kwargs):
        item_name = request.data.get('item_name')
        if not item_name:
            return Response({"error": "Item name is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            inventory_item = Inventory.objects.get(item_name=item_name)
        except Inventory.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = InventorySerializer(inventory_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListInventoryView(APIView):
    def get(self, request, *args, **kwargs):
        inventory_items = Inventory.objects.all()
        serializer = InventorySerializer(inventory_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
