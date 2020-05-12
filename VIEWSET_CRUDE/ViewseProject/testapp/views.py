from django.shortcuts import render
from rest_framework import viewsets
from testapp.models import Students
from testapp.serializers import StudentSerializer
from rest_framework import permissions
# Create your views here.

class StudentViewset(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
#    #permissions_class = (permissions.IsAuthenticated)
