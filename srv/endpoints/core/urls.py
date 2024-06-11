from django.urls import path, re_path, include
from rest_framework.reverse import reverse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Climate API",
      default_version='v1',
      description="Pass-through for location-specific OpenWeatherAPI data.",
      terms_of_service="",
      contact=openapi.Contact(email=""),
      license=openapi.License(name=""),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(
        r'^v1/climate',
        include(('climate.urls','climate'))
    ),
    re_path(
        '^v1/inventory/',
        include(('inventory.urls', 'inventory'))
    ),
    re_path(
        r'^v1/omnipresence',
        include(('omnipresence.urls', 'omnipresence'))
    )
]
