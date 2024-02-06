from django.db import models

# Create your models here.

from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    deadline = models.CharField(max_length=200)
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
