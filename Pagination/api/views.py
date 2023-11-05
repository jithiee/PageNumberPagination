from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import Student
from .serializer import StudnetSeralizer
from .mypagination import MyPageNumberPagination

# Create your views here.

class StudentModelapiView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudnetSeralizer
    pagination_class = MyPageNumberPagination
    