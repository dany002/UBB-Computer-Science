from rest_framework import generics

from employee.models import Employee
from employee.serializers import DynamicEmployeeSerializer, EmployeeSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
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
