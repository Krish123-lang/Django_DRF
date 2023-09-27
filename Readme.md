# Creating Basic API
1. `django-admin startproject project`
2. `python3 manage.py startapp api`
3. `settings.py`
```
INSTALLED_APPS = [
"rest_framework",
"api"
]
```
4. `models.py`
```
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```
5. `admin.py`
```
from .models import *

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
```
6. `serializers.py`
```
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
```
7. `views.py`
```
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Model Object - Single Student Data

def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data, safe=False)

# All Student details

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')

    return JsonResponse(serializer.data, safe=False)
```
8. `urls.py (project)`
```
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('stuinfo/<int:pk>', views.student_detail, name="stuinfo"),
    path('stuinfo', views.student_list, name="stu_list"),
]
```
### Testing (optional)
9. `myapi.py`
```
# Fetching API
import requests

r = requests.get('http://localhost:8000/stuinfo/1')
# print(r.status_code)
js = r.json()
print(js)
```