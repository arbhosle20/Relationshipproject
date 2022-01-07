from django.db import models
from DepartmentApp .models import Dept

class Student(models.Model):
    dept = models.ForeignKey(Dept,on_delete=models.CASCADE,related_name='department_stu')
    rn= models.IntegerField(unique=True)
    name= models.CharField(max_length=50)
    marks = models.FloatField()

    def __str__(self):
        return f"{self.rn},{self.name}"

# Create your models here.
