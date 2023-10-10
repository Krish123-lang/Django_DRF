### If you want Auth and Permissions globally (To all classes)

1. `settings.py`
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```
2. `urls.py`
```
from django.urls import include, path
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentapi', views.StudentViewSet, basename='studentapi')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),

    # *** *** For Authentication *** ***
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
```
3. `views.py`
```
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import viewsets

# For authentication 
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

# For Permissions
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Only if you want to apply auth and permissions to individual class
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # Anyone can access this class (This will override global settings)
    # permission_classes = [AllowAny]

    # Only Admin and staff = True can access
    # permission_classes = [IsAdminUser]

    # *** *** FOR SESSION AUTHENTICATION *** ***
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    # Anyone can access this class (No Login Required)
    # permission_classes = [AllowAny]

    # Only Admin can access (JUST ADMIN)
    # permission_classes = [IsAdminUser]

    # *** *** FOR AUTHENTICATION OR READ-ONLY *** ***
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # *** *** FOR Django Model Permissions *** ***
    # permission_classes = [DjangoModelPermissions]

    # *** *** FOR Django Model ReadOnly Permissions *** ***
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
```