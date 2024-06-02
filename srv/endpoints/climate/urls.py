from . import views
from django.urls import re_path, path

urlpatterns  = [
    re_path(r'^$', views.ClimateDataViewAll.as_view(), name = "climate-all")
]
