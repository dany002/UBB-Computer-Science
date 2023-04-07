from django.urls import path
from employee.Views import EmployeeViews, TeamViews, TaskViews, ProjectViews, views

urlpatterns = [
    path('employees/', EmployeeViews.EmployeeList.as_view()),
    path('employees/<int:pk>/', EmployeeViews.EmployeeDetail.as_view()),
    path('teams/', TeamViews.TeamList.as_view()),
    path('teams/<int:pk>/', TeamViews.TeamDetailView.as_view()),
    path('tasks/', TaskViews.TaskList.as_view()),
    path('tasks/<int:pk>/', TaskViews.TaskDetail.as_view()),
    path('employeeswage/<int:wage>/', EmployeeViews.MinimumWage.as_view()),
    path('projects/', ProjectViews.ProjectList.as_view()),
    path('projects/<int:pk>/',ProjectViews.ProjectDetailView.as_view()),
    path('projects/<int:pk>/teams/', views.ProjectTeamsList.as_view()),
    path('projects/by-avg-difficulty/', views.ProjectsByAvgDifficulty.as_view(), name='projects-by-avg-difficulty'),
    path('teams/by-avg-wage/', views.TeamsByAvgWage.as_view(), name='teams-by-avg-wage'),
    path('employees/by-avg-difficulty/', views.EmployeesByAvgDifficulty.as_view(), name='employees-by-avg-difficulty'),
    path('teams/<int:pk>/employees/', views.EmployeeTeamView.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)