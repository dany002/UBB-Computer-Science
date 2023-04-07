from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from employee.models import Team
from employee.serializers import TeamSerializer, TeamDetailSerializer

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetailView(APIView):

    def get_team(self, pk):
        try:
            return Team.objects.get(id=pk)
        except Team.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        team = self.get_team(pk)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        team = self.get_team(pk)
        serializer = TeamDetailSerializer(team)

        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        team = self.get_team(pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


