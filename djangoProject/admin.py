from django.contrib import admin
from djangoProject.models import *
@admin.register(CompanyModel)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    pass
