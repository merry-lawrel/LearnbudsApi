from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from rest_framework import serializers
from .serializer import EmployeeSerializer

class EmployeeView(APIView):
    def get(self, request):
        # Retrieve all Person objects
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new Person object
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # Update an existing Person object
        try:
            emp = Employee.objects.get(id=request.data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(emp, data=request.data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        # Partially update an existing Person object
        try:
            emp = Employee.objects.get(id=request.data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(emp, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        # Delete a Person object
        try:
            emp = Employee.objects.get(id=request.data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        emp.delete()
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)