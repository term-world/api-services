from django.urls import path
from .views import AddInventoryView, DropInventoryView, UpdateInventoryView, ListInventoryView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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

app_name = 'inventory'

urlpatterns = [
    path('add/', AddInventoryView.as_view(), name='inventory-add'),  # Route for adding items
    path('drop/', DropInventoryView.as_view(), name='inventory-drop'),  # Route for dropping items
    path('update/', UpdateInventoryView.as_view(), name='inventory-update'),  # Route for updating items
    path('', ListInventoryView.as_view(), name='inventory-list'),  # Route for listing all items
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger documentation
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Redoc documentation
]
