from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from omnipresence.serializer import OmnipresenceSerializer

class OmnipresenceView(APIView):

    def post(self, request, *args, **kwargs):
        data = {
            'user': request.data.get('user'),
            'char': request.data.get('char'),
            'cwd': request.data.get('cwd')
        }
        print(data)
        #serializer = OmnipresenceSerializer(data = data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data, status = 201)
        #return Response(serializer.errors, status = 400)
