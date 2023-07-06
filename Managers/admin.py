from django.contrib import admin

# Register your models here.
from .models import Managers
class ManagersAdmin(admin.ModelAdmin):
   list_display=("name","id_number","image","worktime","salary","description","date_hired","date_updated")


admin.site.register(Managers,ManagersAdmin)
 