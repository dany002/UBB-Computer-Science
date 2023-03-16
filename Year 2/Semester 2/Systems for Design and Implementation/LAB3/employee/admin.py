from django.contrib import admin

from employee.models import Employee, Team, Task

# Register your models here.
admin.site.register(Employee)
admin.site.register(Team)
admin.site.register(Task)