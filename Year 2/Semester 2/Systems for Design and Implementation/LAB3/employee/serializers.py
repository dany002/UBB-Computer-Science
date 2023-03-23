from django.db.models import Avg
from rest_framework import serializers

from employee.models import Employee, Team, Task, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('__all__')

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
    firstName = serializers.CharField(max_length=50)
    lastName = serializers.CharField(max_length=50)
    employmentDate = serializers.DateField()
    phoneNumber = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=30)
    wage = serializers.IntegerField()
    created = serializers.DateTimeField()
    team = TeamSerializer(read_only=True)


    def validate_team_id(self, value):
        filter = Team.objects.filter(id=value)
        if not filter.exists():
            raise serializers.ValidationError("Team doesn't exist!")
        return value


    class Meta:
        model = Employee
        fields = ('__all__')
        #fields = ('id', 'firstName', 'lastName', 'employmentDate', 'phoneNumber', 'email', 'wage', 'team_id', 'teamEmployee')

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
class DynamicEmployeeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'firstName', 'lastName', 'employmentDate', 'phoneNumber', 'email', 'wage', 'team_id']

class EmployeeSerializerWithoutTeam(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'firstName', 'lastName', 'employmentDate', 'phoneNumber', 'email', 'wage')

class DynamicTeamSerializer(DynamicFieldsModelSerializer):
    nameOfTeam = serializers.CharField(max_length=100)
    freePlaces = serializers.IntegerField()
    purpose = serializers.CharField(max_length=50)
    admin = serializers.CharField(max_length=50)
    rating = serializers.IntegerField()
    teamEmployee = EmployeeSerializerWithoutTeam(many=True, read_only=True)

    class Meta:
        model = Team
        fields = [ 'nameOfTeam', 'freePlaces', 'purpose', 'admin', 'rating', 'teamEmployee']


class ProjectTeamSerializer(DynamicFieldsModelSerializer):
    team_id = serializers.IntegerField()
    project_id = serializers.IntegerField(default=id)
    #print("id = ",id)
    teamTask = TeamSerializer(many=True, read_only=True)
    projectTask = ProjectSerializer(read_only=True)
    #print("HEHE")
    # firstName = serializers.CharField(max_length=50)
    # lastName = serializers.CharField(max_length=50)
    # employmentDate = serializers.DateField()
    # phoneNumber = serializers.CharField(max_length=20)
    # email = serializers.CharField(max_length=30)
    # wage = serializers.IntegerField()
    # created = serializers.DateTimeField()
    # freePlaces = serializers.IntegerField()
    # purpose = serializers.CharField(max_length=50)
    # admin = serializers.CharField(max_length=50)
    # rating = serializers.IntegerField()
    nameOfTask = serializers.CharField(max_length=200)
    difficulty = serializers.CharField(max_length=200)
    class Meta:
        model = Task
        fields = ['id', 'created', 'nameOfTask', 'difficulty', 'teamTask', 'projectTask', 'team_id', 'project_id']
        #fields = ['__all__']
        #fields = ('teamTask', 'projectTask', 'created', 'nameOfTask', 'difficulty')
        #fields = ['id', 'firstName', 'lastName', 'employmentDate', 'phoneNumber', 'email', 'wage', 'team_id', 'purpose', 'admin', 'rating', 'freePlaces', 'created', 'teamTask', 'projectTask', 'difficulty', 'nameOfTask', 'project_id']


class EmployeeWageSerializer(serializers.ModelSerializer):
    avg_wage = serializers.FloatField()

    class Meta:
        model = Employee
        fields = ('id', 'created', 'email', 'employmentDate', 'firstName', 'lastName', 'phoneNumber', 'avg_wage')

class TeamsByAvgWageSerializer(serializers.ModelSerializer):
    avg_wage = serializers.FloatField()

    class Meta:
        model = Team
        fields = ('id', 'created', 'nameOfTeam', 'freePlaces', 'purpose', 'admin', 'rating', 'avg_wage')


# class ProjectsByAvgDifficultySerializer(serializers.ModelSerializer):
#     avg_difficulty = serializers.FloatField()
#
#     class Meta:
#         model = Project
#         fields = ('id', 'created', 'nameOfProject', 'clientName', 'budget', 'description', 'status', 'avg_difficulty')

class ProjectsByAvgDifficultySerializer(serializers.ModelSerializer):
    avg_difficulty = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id', 'created', 'nameOfProject', 'clientName', 'budget', 'description', 'status', 'avg_difficulty')

    def get_avg_difficulty(self, obj):
        avg_diff = obj.projectTask.aggregate(Avg('difficulty'))['difficulty__avg']
        return avg_diff if avg_diff else 0