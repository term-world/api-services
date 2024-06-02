from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import AllowAny

from climate.models import TransientModel
from climate.serializers import TransientModelSerializer

class ClimateDataViewAll(APIView):

    permission_classes = [AllowAny]
    serializer_class = TransientModelSerializer

    def get(self, request, format=None):
        return TransientModel.obj.all()
        #return JsonResponse({"!":"."}, status = 200)
