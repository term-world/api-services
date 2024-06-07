from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory
from .serializers import InventorySerializer
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

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

class InventoryView(APIView):
    def get(self, request, *args, **kwargs):
        item_id = kwargs.get('item_id')
        if item_id:
            try:
                inventory_item = Inventory.objects.get(pk=item_id)
                serializer = InventorySerializer(inventory_item)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Inventory.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            inventory_items = Inventory.objects.all()
            serializer = InventorySerializer(inventory_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        item_id = kwargs.get('item_id')
        inventory_item = Inventory.objects.get(pk=item_id)
        serializer = InventorySerializer(inventory_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)