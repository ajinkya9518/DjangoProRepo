from django.shortcuts import render
from testapp.models import Newspaper
from testapp.serializers import NewspaperSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication#
from rest_framework.permissions import IsAuthenticated#

# Create your views here.
class NewspaperList(APIView):
    def get(self,request):
        newspaper = Newspaper.objects.all()
        serializer = NewspaperSerializer(newspaper,many=True)
        #authentication_classes = [TokenAuthentication,]
        #permission_classes = [IsAuthenticated,]
        return Response (serializer.data)

    def post(self,request):
        serializer = NewspaperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class NewspaperDetail(APIView):
    def get_object(self,pk):
        try:
            return Newspaper.objects.get(pk=pk)
        except Newspaper.DoesNotExist:
            return Response (status = status.HTTP_404_NOT_FOUND)

    def get(self,request,pk,format = None):
        newspaper = self.get_object(pk=pk)
        serializer = NewspaperSerializer(newspaper)
        return Response(serializer.data)

    def put(self,request,pk,format = None):
        newspaper = self.get_object(pk=pk)
        serializer = NewspaperSerializer(newspaper,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk = None):
        newspaper = self.get_object(pk=pk)
        newspaper.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
