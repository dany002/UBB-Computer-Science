from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from employee.models import Project
from employee.serializers import ProjectSerializer, ProjectDetailSerializer



class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()[:100]
    serializer_class = ProjectSerializer

class ProjectDetailView(APIView):
    lookup_url_kwarg = "pk"
    def get_project(self, pk):
        try:
            return Project.objects.get(id=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializer = ProjectDetailSerializer(project)
        print(serializer.data)
        return Response(serializer.data)
