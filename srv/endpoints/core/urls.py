from django.urls import path, include

urlpatterns = [
    path('v1/climate/', include('climate.urls', namespace='climate')),
    path('v1/inventory/', include('inventory.urls', namespace='inventory')),
]
