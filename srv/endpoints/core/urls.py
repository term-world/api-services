from django.urls import path, re_path, include
from rest_framework.reverse import reverse

urlpatterns = [
    re_path(
        r'^v1/climate',
        include(('climate.urls','climate'))
    ),
    re_path(
        r'^v1/omnipresence',
        include(('omnipresence.urls', 'omnipresence'))
    )
]
