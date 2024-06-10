from . import views
from django.urls import re_path, path

urlpatterns  = [
    re_path('update/(?P<pk>\d+)', views.OmnipresenceUpdateView.as_view(), name = "omnipresence-update"),
    re_path('$', views.OmnipresenceView.as_view(), name = "omnipresence-post"),
]
