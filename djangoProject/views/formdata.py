from rest_framework.views import APIView
from rest_framework.response import Response

from djangoProject.models import *
from djangoProject.serializers import *

class UploadJson(APIView):
    # Defining POST method
    def post(self, request):

        # Initializing JSON depth variables
        companyData = request.data["company"] # returns an object
        employeeData = request.data["company"]["employees"] # returns an array of objects

        # Initializing serializers
        compSerializer = CompanySerializer(data=companyData)

        # Create the company model, if serializer is correct
        if(compSerializer.is_valid()):
            compSerializer.save()
            # return Response(data=compSerializer.data, status=200)
        else:
            return Response(data=compSerializer.errors, status=400)

        # Getting the total number of the employees
        totalEmployeeCount = EmployeeModel.objects.count()

        # Checking if the total number of employees is greater than 100000 and returning an error if it is true
        if (totalEmployeeCount > 100000):
            return Response(data="The number of employees must be less than 100.000", status=400)

        # Get the ID of the newly created company model
        last_id = CompanyModel.objects.last().id

        # Adding the company ID to the employee list
        instanceCounter = 0;
        for x in employeeData:
            x["company"] = last_id
            instanceCounter += 1

        # Form validation component that checks the number of employees
        if (instanceCounter > 100 or instanceCounter < 1):
            return Response(data="Number of employees must be a positive integer, at least 1 and maximum 100", status=400)

        # Serializing employees
        empSerializer = EmployeeSerializer(data=employeeData, many=True)

        # Saving employees if validation is correct
        if(empSerializer.is_valid()):
            empSerializer.save()
            return Response(data="Company and employees sucessfully saved", status=200)
        else:
            return Response(data=empSerializer.errors, status=400)