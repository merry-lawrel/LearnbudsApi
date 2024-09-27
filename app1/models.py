from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    # Fields for Employee
    name = models.CharField(max_length=50)
    stack = models.CharField(max_length=50)
    experience = models.IntegerField()
    location = models.CharField(max_length=100)