from . import views
from django.urls import re_path, path

urlpatterns  = [
    re_path(r'^$', views.OmnipresenceView.as_view(), name = "omnipresence")
]
