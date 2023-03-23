from django.db.models import Avg
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from employee.models import Employee, Team, Task, Project
from employee.serializers import EmployeeSerializer, TeamSerializer, TaskSerializer, DynamicEmployeeSerializer, \
    DynamicTeamSerializer, ProjectSerializer, ProjectTeamSerializer, TeamsByAvgWageSerializer, \
    ProjectsByAvgDifficultySerializer


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = DynamicTeamSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    #serializer_class = EmployeeSerializer
    serializer_class = DynamicEmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class MinimumWage(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = "wage"

    def get_queryset(self):
        queryset = Employee.objects.all()
        wage = self.kwargs.get(self.lookup_url_kwarg)
        if wage is not None:
            queryset = queryset.filter(wage__gt=wage)
        return queryset

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectTeamsList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectTeamSerializer
    lookup_url_kwarg = "pk"
    def get_queryset(self):
        queryset = Task.objects.all()
        #print("HI")
        primaryKey = self.kwargs.get(self.lookup_url_kwarg)
        queryset = queryset.filter(project_id=primaryKey)
        #print(len(queryset))
        #print(queryset)
        return queryset

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