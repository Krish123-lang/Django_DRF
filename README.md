# Deserialization
1. `settings.py`
```
INSTALLED_APPS = [
    'rest_framework',
    'api',
]
```
2. `models.py`
```
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```
3. `admin.py`
```
from .models import *

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
```
4. `serializers.py`
```
from rest_framework import serializers
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)
```
5. `views.py`
```
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
```
6. `urls.py (project)`
```
from api.views import student_create

urlpatterns = [
    path("admin/", admin.site.urls),
    path('stucreate', student_create, name="stucreate")
]
```
7. `myapi.py (Testing)`
```
import requests
import json

url = 'http://localhost:8000/stucreate'

data = {
    'id': 20,
    'name': 'Mark',
    'roll': 20,
    'city': 'Kathmandu'
}

json_data = json.dumps(data)
r = requests.post(url=url, data=json_data)
data = r.json()
print(data)
```