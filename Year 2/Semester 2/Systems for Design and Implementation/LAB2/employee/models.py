from django.db import models
import uuid
# Create your models here.

class Team(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nameOfTeam = models.CharField(max_length=100)
    freePlaces = models.IntegerField()
    purpose = models.CharField(max_length=200)
    admin = models.CharField(max_length=200)
    rating = models.IntegerField()

    def __str__(self):
        return self.nameOfTeam

    class Meta:
        ordering = ['created']

class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nameOfTask = models.CharField(max_length=200)
    daysToImplement = models.IntegerField()
    difficulty = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    taken = models.BooleanField(default=False)

    def __str__(self):
        return self.nameOfTask

    class Meta:
        ordering = ['created']

class Employee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE) # 1 to many; a team can have more employees.
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    employmentDate = models.DateField()
    phoneNumber = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    wage = models.IntegerField()

    def __str__(self):
        return self.firstName + " " + self.lastName + " " + self.email
    class Meta:
        ordering = ['created']



