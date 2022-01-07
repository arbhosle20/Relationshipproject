from django.db import models

class Dept(models.Model):
    name = models.CharField(max_length=50)
    intake = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


# Create your models here.
