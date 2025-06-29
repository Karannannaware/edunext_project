from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet, InstructorViewSet, StudentViewSet,
    home, index, StudentRegisterView, CustomLoginView
)

# ✅ DRF Router for ViewSets
router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'instructors', InstructorViewSet)
router.register(r'students', StudentViewSet)

# ✅ URL patterns
urlpatterns = [
    path('', index, name='index'),                        # HTML page
    path('home/', home, name='home'),                     # Text page
    path('api/', include(router.urls)),                   # All viewsets at /api/

    # 🔐 Custom Auth APIs
    path('api/register-student/', StudentRegisterView.as_view(), name='register-student'),
    path('api/login/', CustomLoginView.as_view(), name='custom-login'),
]
