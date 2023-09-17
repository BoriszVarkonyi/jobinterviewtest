from djangoProject.models import *
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = [
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