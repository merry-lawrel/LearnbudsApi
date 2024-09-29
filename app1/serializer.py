from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee  # Specify the model to be serialized
        fields = ['id', 'name', 'stack', 'experience', 'location']  # Specify the fields to be included in the serialized output

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self,data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError("Username already exists")

        if data['email']:
            if User.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError("Emailalready exists")

        return data

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'], email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()