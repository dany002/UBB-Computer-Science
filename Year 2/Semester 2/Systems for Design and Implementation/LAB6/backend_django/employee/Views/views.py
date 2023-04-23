from django.db.models import Avg
from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from employee.models import Employee, Team, Task, Project
from employee.serializers import EmployeeSerializer, TeamSerializer, DynamicEmployeeSerializer, \
    DynamicTeamSerializer, ProjectSerializer, ProjectTeamSerializer, TeamsByAvgWageSerializer, \
    ProjectsByAvgDifficultySerializer, TaskSerializer2, EmployeesByAvgDifficultySerializer, TeamEmployeeSerializer, \
    ProjectDetailSerializer, TeamDetailSerializer


class ProjectTeamsList(APIView):

    def get_object(self, pk):
        try:
            return Task.objects.get(project_id=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tasks = Task.objects.all()
        tasks = tasks.filter(project_id=pk)

        serializer = ProjectTeamSerializer(tasks,many=True)
        #serializer = TaskSerializer2(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 # User review product/1/users;
    def post(self, request, pk, format=None):
        try:
            team_id = request.data["team"]
            project = Project.objects.get(id=pk)
            team = Team.objects.get(id=team_id)
            task = Task(project=project, team=team)
            task.difficulty = request.data.get("difficulty")
            task.nameOfTask = request.data.get("nameOfTask")
            task.save()
            serializer = TaskSerializer2(task)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except (Team.DoesNotExist, Project.DoesNotExist):
            return Response({"error" : "Invalid team or project id"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ProjectsByAvgDifficulty(APIView):
    def get(self, request):
        queryset = Project.objects.annotate(avg_difficulty=Avg('projectTask__difficulty')).order_by('-avg_difficulty')
        serializer = ProjectsByAvgDifficultySerializer(queryset, many=True)
        return Response(serializer.data)

class TeamsByAvgWage(APIView):
    def get(self, request):
        queryset = Team.objects.annotate(avg_wage=Avg('teamEmployee__wage')).order_by('-avg_wage')
        serializer = TeamsByAvgWageSerializer(queryset, many=True)
        return Response(serializer.data)


class EmployeesByAvgDifficulty(APIView):
    def get(self, request):
        queryset = Employee.objects.annotate(avg_difficulty=Avg('team__teamTask__difficulty')).order_by('-avg_difficulty')
        serializer = EmployeesByAvgDifficultySerializer(queryset, many=True)
        return Response(serializer.data)

class EmployeeTeamView(APIView):
    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404

    def get_employee(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        team = self.get_object(pk)
        employee_ids = request.data['list_of_ids']
        employees = []
        for i in range(len(employee_ids)):
            employee = self.get_employee(employee_ids[i])
            employee.team_id = pk
            employee.save()
            employees.append(employee)
        serializer = TeamEmployeeSerializer(employees[0],data=model_to_dict(employees[0]))

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

