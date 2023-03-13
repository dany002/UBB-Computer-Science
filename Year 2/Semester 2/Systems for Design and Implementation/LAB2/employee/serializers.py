from rest_framework import serializers

from employee.models import Employee, Team, Task


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('__all__')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')


class EmployeeSerializer(serializers.ModelSerializer):
    team_id = serializers.IntegerField(write_only=True)
    team = TeamSerializer(many=True, read_only=True)
    firstName = serializers.CharField(max_length=50)
    lastName = serializers.CharField(max_length=50)
    employmentDate = serializers.DateField()
    phoneNumber = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=30)
    wage = serializers.IntegerField()

    def validate_team_id(self, value):
        filter = Team.objects.filter(id=value)
        if not filter.exists():
            raise serializers.ValidationError("Team doesn't exist!")
        return value


    class Meta:
        model = Employee
        fields = ('id', 'firstName', 'lastName', 'employmentDate', 'phoneNumber', 'email', 'wage', 'team_id', 'team')
