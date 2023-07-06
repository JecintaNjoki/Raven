from django.contrib import admin

# Register your models here.
from .models import Employees
class EmployeesAdmin(admin.ModelAdmin):
   list_display=("name","id_number","image","worktime","salary","description","date_hired","date_updated")


admin.site.register(Employees,EmployeesAdmin)
 
        