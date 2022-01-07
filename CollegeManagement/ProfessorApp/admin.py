from django.contrib import admin
from .models import Prof

class ProfAdmin(admin.ModelAdmin):
    list_display = ['name','salary']
admin.site.register(Prof,ProfAdmin)

# Register your models here.
