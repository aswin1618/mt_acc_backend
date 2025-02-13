from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListCreateAPIView(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        if not employees:  
            return Response({"message": "No employees found"}, status=200)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=200) 

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employee added successfully!", "data": serializer.data}, status=201)
        else: 
            return Response({"error": serializer.errors}, status=400)

class EmployeeDetailAPIView(APIView):

    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)
        
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employee updated!", "data": serializer.data}, status=202)
        
        return Response(serializer.errors, status=400) 

    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response({"message": "Employee deleted successfully"}, status=204) 
