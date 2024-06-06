from django.urls import path
from .views import InventoryView

urlpatterns = [
    path('inventory/', InventoryView.as_view(), name='inventory-post'),
    path('inventory/<int:item_id>/', InventoryView.as_view(), name='inventory-update'),
]