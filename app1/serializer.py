from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee  # Specify the model to be serialized
        fields = ['id', 'name', 'stack', 'experience', 'location']  # Specify the fields to be included in the serialized output