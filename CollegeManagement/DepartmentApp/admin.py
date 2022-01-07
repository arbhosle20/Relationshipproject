from django.contrib import admin
from DepartmentApp.models import Dept

class DeptAdmin(admin.ModelAdmin):
    list_display = ['name','intake']
admin.site.register(Dept,DeptAdmin)
# Register your models here.
