from api.models import Student
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
