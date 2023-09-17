from rest_framework.views import APIView
from rest_framework.response import Response

from djangoProject.models import *
from djangoProject.serializers import *

class DisplayData(APIView):
    def get(self, request):

        companies = CompanyModel.objects
        serializedCompanies = CompanySerializer(companies, many=True)

        employees = EmployeeModel.objects
        serializedEmployees = EmployeeSerializer(employees, many=True)

        companyDict = {}

        for x in serializedCompanies.data:
            companyDict[x['id']] = x["name"]

        joinedDict = {}

        for key, value in companyDict.items():
            compEmployees = []
            for z in serializedEmployees.data:
                if (key == z["company"]):
                    compEmployees.append(z)
            joinedDict[value] = compEmployees


        return Response(data=joinedDict, status=200)
