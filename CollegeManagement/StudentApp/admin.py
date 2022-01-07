from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['dept','rn','name','marks']
admin.site.register(Student,StudentAdmin)

# Register your models here.
