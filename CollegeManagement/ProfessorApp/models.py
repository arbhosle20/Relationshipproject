from django.db import models
from DepartmentApp .models import Dept


class Prof(models.Model):
    dept = models.ManyToManyField(Dept,related_name='department_pro')
    name = models.CharField(max_length=50)
    salary = models.FloatField()

    def __str__(self):
        return f"{self.name},{self.salary}"


# Create your models here.
