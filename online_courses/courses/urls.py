from rest_framework.routers import DefaultRouter
from .views import ProfessorViewSet, CourseViewSet, StudentViewSet, EnrollmentViewSet, LessonViewSet

# Criação do roteador
router = DefaultRouter()
router.register('professors', ProfessorViewSet)
router.register('courses', CourseViewSet)
router.register('students', StudentViewSet)
router.register('enrollments', EnrollmentViewSet)
router.register('lessons', LessonViewSet)

# Configurando as URLs
urlpatterns = router.urls
