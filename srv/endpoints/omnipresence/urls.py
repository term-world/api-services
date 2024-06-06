from . import views
from django.urls import re_path, path

urlpatterns  = [
    re_path('', views.OmnipresenceView.as_view(), name = "omnipresence-post"),
    path('<str:username>/', views.OmnipresenceView.as_view(), name = "omnipresence-update")
]
