from django.http import Http404, JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from employee.models import Team
from employee.serializers import TeamSerializer, TeamDetailSerializer
from rest_framework.decorators import api_view

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()[:100]
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



@api_view(['GET'])
def get_teams_pagination(request, page=1):
    # get all the team members from the database
    team_members = Team.objects.all()

    # set the number of items per page
    items_per_page = 10

    # calculate the start and end indices for the current page
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page

    # slice the team members based on the start and end indices
    team_members_slice = team_members[start_index:end_index]

    # calculate the total number of pages
    total_pages = (team_members.count() + items_per_page - 1) // items_per_page

    # create a dictionary containing the paginated data
    data = {
        'team_members': list(team_members_slice.values()),
        'current_page': page,
        'total_pages': total_pages,
        'items_per_page': items_per_page
    }

    # return the paginated data as a JSON response
    return JsonResponse(data)
