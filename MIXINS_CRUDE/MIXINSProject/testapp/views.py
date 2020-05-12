from django.shortcuts import render
from testapp.models import Mobile
from testapp.serializers import MobileSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
# Create your views here.

class MobileList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class MobileDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)
