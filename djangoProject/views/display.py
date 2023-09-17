from rest_framework.views import APIView
from rest_framework.response import Response

from djangoProject.models import *
from djangoProject.serializers import *

class DisplayData(APIView):
    def get(self, request):

        # Serialize all companies
        companies = CompanyModel.objects
        serializedCompanies = CompanySerializer(companies, many=True)

        # Serialize all employees
        employees = EmployeeModel.objects
        serializedEmployees = EmployeeSerializer(employees, many=True)

        # Creating empty dictionary for storing all company data
        companyDict = {}

        # Filling empty dictionary with company data
        for x in serializedCompanies.data:
            companyDict[x['id']] = x["name"]

        # Creating empty dictionary for joined values
        joinedDict = {}

        # Merging company id's with employees assigned company id's to assign employees to dictionaries
        for key, value in companyDict.items():
            compEmployees = []
            for z in serializedEmployees.data:
                if (key == z["company"]):
                    compEmployees.append(z)
            joinedDict[value] = compEmployees

        # Returning merged dictionary
        return Response(data=joinedDict, status=200)
