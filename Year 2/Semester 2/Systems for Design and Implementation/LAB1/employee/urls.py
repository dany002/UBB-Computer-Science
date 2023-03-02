from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from employee import views

urlpatterns = [
    path('employees/', views.EmployeeList.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)