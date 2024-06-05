from django.urls import path, re_path, include
from rest_framework.reverse import reverse
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Climate API')

urlpatterns = [
    path('v1/climate/', include('climate.urls')),
    path('v1/climate/docs/', schema_view)
]
