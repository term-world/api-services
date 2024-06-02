from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

class ClimateDataViewAll(APIView):
    def get(self, request, format=None):
        return JsonResponse({"!":"."}, status = 200)
