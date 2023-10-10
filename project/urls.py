from django.contrib import admin
from django.urls import include, path
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentapi', views.StudentViewSet, basename='studentapi')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),

    # *** *** For Session Authentication *** ***
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
