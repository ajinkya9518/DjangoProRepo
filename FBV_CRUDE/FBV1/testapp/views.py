from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerialier
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET','POST'])
def employee_list(request):
    if request.method == "GET":
        employees = Employee.objects.all()
        serializer = EmployeeSerialier(employees,many=True)
        return Response (serializer.data)

    elif request.method == "POST":
        serializer = EmployeeSerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def employee_detail(request,pk):
    try:
        employees = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = EmployeeSerialier(employees)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = EmployeeSerialier(employees,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        employees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
