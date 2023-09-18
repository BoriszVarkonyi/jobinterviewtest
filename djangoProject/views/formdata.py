from builtins import object

from rest_framework.views import APIView
from rest_framework.response import Response

from djangoProject.serializers import *


class CompanyData(APIView):
    """
    This function defines the POST method

    The following function takes a request parameter. request.data contains all the necessary information to
    create the company instances and then the according employee instances.

    @param object request *stores the posted JSON data*

    @return object Response *Response object returns the error messages, if there were any, or the message of
    acceptance with the matching HTTP status code*

    """
    def post(self, request):

        # Initializing JSON depth variables
        if 'company' in request.data:
            companyData = request.data["company"]  # returns an object
        else:
            return Response(data="No company object was fount", status=400)

        if 'employees' in request.data["company"]:
            employeeData = request.data["company"]["employees"] # returns an array of objects
        else:
            return Response(data="No employee array was fount", status=400)

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
        instanceCounter = 0
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

    """
    This function defines the GET method
    
    The following function displays all the company instances with the related employee instances stored as a related
    field which is an array of objects.
    
    @return object Response *The Response object returns a serialized JSON as data and a corresponding HTTP status code
    if the request was successful*  
    """

    def get(self, request):
        companies = CompanyModel.objects
        serializedCompanies = DisplaySerializer(companies, many=True)
        return Response(data=serializedCompanies.data, status=200)
