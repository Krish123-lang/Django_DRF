from django.shortcuts import render

# Create your views here.
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import viewsets


# For authentication and Permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
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