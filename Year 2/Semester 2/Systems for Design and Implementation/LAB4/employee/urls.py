from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from employee import views

urlpatterns = [
    path('employees/', views.EmployeeList.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('teams/', views.TeamList.as_view()),
    path('teams/<int:pk>/', views.TeamDetail.as_view()),
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('employeeswage/<int:wage>/', views.MinimumWage.as_view()),
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>',views.ProjectDetail.as_view()),
    path('projects/<int:pk>/teams', views.ProjectTeamsList.as_view()),
    path('projects/by-avg-difficulty', views.ProjectsByAvgDifficulty.as_view(), name='projects-by-avg-difficulty'),
    path('teams/by-avg-wage', views.TeamsByAvgWage.as_view(), name='teams-by-avg-wage'),
    path('employees/by-avg-difficulty', views.EmployeesByAvgDifficulty.as_view(), name='employees-by-avg-difficulty'),
    path('team/<int:pk>/employees/', views.EmployeeTeamView.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)