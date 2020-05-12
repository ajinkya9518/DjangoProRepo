from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import City
from .seriliazers import  CitySerializer
# Create your views here.

class CityViewset(viewsets.ModelViewSet):
    permission_class = (permissions.IsAuthenticated,)
    query_set = City.objects.all()
    serializer_class = CitySerializer
