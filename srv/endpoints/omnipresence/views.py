from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from omnipresence.serializer import OmnipresenceSerializer

class OmnipresenceView(APIView):

    def post(self, request, *args, **kwargs):
        data = {
            'username': request.data.get('username'),
            'charname': request.data.get('charname'),
            'working_dir': request.data.get('working_dir')
        }
        serializer = OmnipresenceSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = 201)
        return Response(serializer.errors, status = 400)

    def put(self, request, *args, **kwargs):
        serializer = OmnipresenceSerializer(data = request.DATA, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(status = 200)
        return Response(serializer.errors, status = 400)
