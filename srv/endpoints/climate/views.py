from rest_framework.generics import ListAPIView
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import AllowAny

from climate.models import ClimateModel
from climate.serializers import ClimateModelSerializer

class ClimateDataViewAll(ListAPIView):

    permission_classes = [AllowAny]
    serializer_class = ClimateModelSerializer

    def get_queryset(self):
        try:
            queryset = ClimateModel.obj.all()
            return queryset
        except Exception as e:
            raise APIException(e) from e
