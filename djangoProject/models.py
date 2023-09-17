from django.db import models
from djangoProject.choices import *
from django.core.validators import MinValueValidator

class CompanyModel(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    description = models.TextField(null=True)

class EmployeeModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)

    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    jobTitle = models.CharField(max_length=256, choices=JOB_TITLE_CHOICE, default="")
    age = models.IntegerField(validators=[MinValueValidator(18)])