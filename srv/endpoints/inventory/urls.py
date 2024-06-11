from django.urls import path
from .views import AddInventoryView, DropInventoryView, UpdateInventoryView, ListInventoryView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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

app_name = 'inventory'

urlpatterns = [
    path('add/', AddInventoryView.as_view(), name='inventory-add'),  # Route for adding items
    path('drop/', DropInventoryView.as_view(), name='inventory-drop'),  # Route for dropping items
    path('update/<int:id>', UpdateInventoryView.as_view(), name='inventory-update'),  # Route for updating items
    path('list', ListInventoryView.as_view(), name='inventory-list'),  # Route for listing all items
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger documentation
]
