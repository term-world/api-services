import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from omnipresence.models import OmnipresenceModel
from omnipresence.serializer import OmnipresenceSerializer

class OmnipresenceView(APIView):

    def get(self, request, *args, **kwargs):
        character = OmnipresenceModel.objects.filter(
            charname = request.GET.get('charname')
        ).values('username','charname','working_dir')
        print(character)
        if character:
            return HttpResponse(
                json.dumps(list(character)),
                status = 200,
                content_type = 'application/json'
        )
        return HttpResponse(json.dumps(dict()), status = 200, content_type = 'application/json')

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
