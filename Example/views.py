from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from rest_framework import generics

from Example.models import Example

from Example.serializer import ExampleSerializers

class ExampleList(APIView):
    #metodo get para solicitar info
    def get(self, request, format=None):
        queryset = Example.objects.filter(delete = False)
        serializer = ExampleSerializers(queryset)
        return response(serializer.data)

# Create your views here.
