from django.shortcuts import render
from testapp.models import PersonalInfo
from testapp.serializers import PersonalInfoSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import permissions
#from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class PersonalInfoList(generics.ListCreateAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permissions_classes = (permissions.IsAuthenticated)
    #authentication_classes = (SessionAuthentication,BasicAuthentication)
    authentication_classes = (TokenAuthentication,)


class PersonalInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permissions_classes = (permissions.IsAuthenticated)
    #authentication_classes = (SessionAuthentication,BasicAuthentication)
    authentication_classes = (TokenAuthentication,)
