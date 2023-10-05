# FUNCTION BASED CRUD API

1. `settings.py`
```
INSTALLED_APPS = [
    "rest_framework",
    "api",
]
```

2. `models.py`
```
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.name
```
3. `admin.py`
```
from django.contrib import admin
from api.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
```

2. `serializers.py`
```
from rest_framework.serializers import Serializer, ModelSerializer
from api.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
```
4. `urls.py`
```
from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # path('studentapi', views.hello_world, name="studentapi")

    path('studentapi', views.student_api, name="studentapi"),
    path('studentapi/<int:pk>/', views.student_api, name="studentapi"),
]
```

3. `views.py`
```
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import status

# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == "GET":
#         return Response({'msg': "This is GET request !"})

#     if request.method == "POST":
#         return Response({'msg': "This is POST request !", 'data': request.data})


# CRUD
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request,pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created !'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated !'})
        return Response(serializer.errors)

    if request.method == "PATCH":
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'PATCH Data Updated !'})
        return Response(serializer.errors)

    if request.method == "DELETE":
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted  !'})
```