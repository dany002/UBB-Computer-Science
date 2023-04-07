from django.db.models import Avg
from rest_framework import serializers

from employee.models import Employee, Team, Task, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('__all__')

class TeamSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data['freePlaces'] < 0:
            raise serializers.ValidationError("Free places should be >= 0")
        return data

    class Meta:
        model = Team
        fields = ('__all__')


class TaskSerializer(serializers.ModelSerializer):
    teamTask = TeamSerializer()
    projectTask = ProjectSerializer()
    class Meta:
        model = Task
        fields = ('__all__')

class TaskSerializer2(serializers.ModelSerializer):
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
    team_id = serializers.IntegerField()

    def validate_team_id(self, value):
        filter = Team.objects.filter(id=value)
        if not filter.exists():
            raise serializers.ValidationError("Team doesn't exist!")
        return value

    def validate(self, data):
        if data['employmentDate'].year > 2023:
            raise serializers.ValidationError("Year has to be less than 2023!")
        return data

    class Meta:
        model = Employee
        fields = ['id', 'firstName', 'lastName', 'employmentDate', 'phoneNumber', 'email', 'wage', 'team_id']



class EmployeeSerializerWithoutTeam(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'created', 'firstName', 'lastName', 'employmentDate', 'phoneNumber', 'email', 'wage')


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


class TeamSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('__all__')


class ProjectTeamSerializer(DynamicFieldsModelSerializer):

    team_id = serializers.IntegerField()
    nameOfTask = serializers.CharField(max_length=200)
    teamTask = TeamSerializer3(many=True, read_only=True)
    projectTask = ProjectSerializer(many=True,read_only=True)

    class Meta:
        model = Task
        fields = ['nameOfTask','difficulty', 'teamTask', 'team_id', 'projectTask']


class EmployeeWageSerializer(serializers.ModelSerializer):
    avg_wage = serializers.FloatField()

    class Meta:
        model = Employee
        fields = ('id', 'created', 'email', 'employmentDate', 'firstName', 'lastName', 'phoneNumber', 'avg_wage')


class TeamsByAvgWageSerializer(serializers.ModelSerializer):
    avg_wage = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ('id', 'created', 'nameOfTeam', 'freePlaces', 'purpose', 'admin', 'rating', 'avg_wage')

    def get_avg_wage(self, obj):
        avg_wagee = obj.teamEmployee.aggregate(Avg('wage'))['wage__avg']
        return avg_wagee if avg_wagee else 0

class ProjectsByAvgDifficultySerializer(serializers.ModelSerializer):
    avg_difficulty = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id', 'created', 'nameOfProject', 'clientName', 'budget', 'description', 'status', 'avg_difficulty')

    def get_avg_difficulty(self, obj):
        avg_diff = obj.projectTask.aggregate(Avg('difficulty'))['difficulty__avg']
        return avg_diff if avg_diff else 0


class EmployeesByAvgDifficultySerializer(serializers.ModelSerializer):
    avg_difficulty = serializers.SerializerMethodField()
    class Meta:
        model = Employee
        fields = ('id', 'firstName', 'lastName', 'employmentDate', 'phoneNumber', 'email', 'wage', 'avg_difficulty')

    def get_avg_difficulty(self, obj):

        avg_dif = obj.team.teamTask.aggregate(Avg('difficulty'))['difficulty__avg']
        return avg_dif if avg_dif else 0



class EmployeeSerializer5(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class TeamEmployeeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Employee
        fields = ['team_id']


class TaskSerializerWithTeamAndWithoutProject(serializers.ModelSerializer):
    created = serializers.DateTimeField()
    nameOfTask = serializers.CharField()
    difficulty = serializers.IntegerField()
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ('created', 'nameOfTask', 'difficulty', 'team')


class ProjectDetailSerializer(DynamicFieldsModelSerializer):
    projectTask = TaskSerializerWithTeamAndWithoutProject(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id','created','nameOfProject','clientName','budget','description','status','projectTask']


class TaskSerializerWithProjectAndWithoutTeam(serializers.ModelSerializer):
    created = serializers.DateTimeField()
    nameOfTask = serializers.CharField()
    difficulty = serializers.IntegerField()
    project = ProjectSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ('id','created', 'nameOfTask', 'difficulty', 'project')


class TeamDetailSerializer(DynamicFieldsModelSerializer):
    teamTask = TaskSerializerWithProjectAndWithoutTeam(many=True, read_only=True)

    teamEmployee = EmployeeSerializerWithoutTeam(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['created','nameOfTeam', 'freePlaces', 'purpose', 'admin', 'rating', 'teamTask', 'teamEmployee']
