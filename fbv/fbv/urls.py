from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('studentapi', views.hello_world, name="studentapi")

    # CRUD
    path('studentapi', views.student_api, name="studentapi"),
    path('studentapi/<int:pk>/', views.student_api, name="studentapi"),
]
