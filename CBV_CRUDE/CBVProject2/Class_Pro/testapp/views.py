from django.shortcuts import render
from .models import Newspaper
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class NewspaperList(APIView):
    def get(self,request):
        news = Newspaper.objects.all()
        serializer = NewsSerializer(news,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = NewsSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class NewsPaperDetail(APIView):
    def get_object(self,pk):
        try:
            return Newspaper.objects.get(pk=pk)
        except news.DoesNotExist:
            return HttpResponse(status=404)

    def get(self,request,pk,format = None):
        news = self.get_object(pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    def put(self,request,pk,format = None):
        news = self.get_object(pk)
        serializer = NewsSerializer(news,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data,status= status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format = None):
        news = self.get_object(pk)
        news.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
