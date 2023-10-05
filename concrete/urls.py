from django.contrib import admin
from django.urls import include, path
from api import views

# === === ViewSet === ===
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('studentapi', views.StudentViewSet, basename='student')

# === === Model ViewSet === === 
# router.register('studentapi', views.StudentModelViewSet, basename='student')

# === === Read-Only Model ViewSet === === 
router.register('studentapi', views.StudentReadOnlyModelViewSet, basename='student')


urlpatterns = [
    path("admin/", admin.site.urls),

    # === === === API View === === ===
    # path('studentapi', views.StudentListCreate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),


    # === === ViewSet === ===
    path('api/', include(router.urls))

]
