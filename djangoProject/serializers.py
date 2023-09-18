from djangoProject.models import *
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = [
            'id',
            'name',
            'email',
            'description'
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = [
            'company',
            'name',
            'email',
            'jobTitle',
            'age'
        ]

class DisplaySerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)
    class Meta:
        model = CompanyModel
        fields = [
            'id',
            'name',
            'email',
            'description',
            'employees'
        ]
