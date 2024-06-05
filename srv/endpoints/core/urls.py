from django.urls import path, re_path, include
from rest_framework.reverse import reverse

urlpatterns = [
    re_path(r'^v1/climate', include(('climate.urls','climate'), namespace='v1')),
    re_path(r'^v1/omnipresence', include(('omnipresence.urls', 'omnipresence'), namespace='v1'))
]
