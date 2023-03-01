from django.db import models
import uuid
# Create your models here.

class Employee(models.Model):
    employeeId = models.CharField(default=str(uuid.uuid1()), max_length=40)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    employmentDate = models.DateField()
    phoneNumber = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    wage = models.IntegerField()
