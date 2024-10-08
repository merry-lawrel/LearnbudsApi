from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Employee
from rest_framework import serializers
from .serializer import EmployeeSerializer, RegisterSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

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

class RegisterAPI(APIView):
    def post(self,request):
        _data = request.data
        serializer = RegisterSerializer(data = _data)

        if not serializer.is_valid():
            return Response({'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)

        serializer.save()

        return Response({'message':'User created'}, status=status.HTTP_201_CREATED)

class LoginAPI(APIView):
    permission_classes = []

    def post(self, request):
        _data = request.data
        serializer = LoginSerializer(data = _data)

        if not serializer.is_valid():
            return Response({'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)

        user = authenticate(username = serializer.data['username'], password = serializer.data['password'])

        if not user:
            return Response({'message': "Invalid"},status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'message': 'Login successful', 'token': str(token)}, status=status.HTTP_200_OK)

class Employee(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        objemployee = Employee.objects.filter(team__isnull=False)
        serializer = EmployeeSerializer(objEmployee, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response("This is a post method api view")
