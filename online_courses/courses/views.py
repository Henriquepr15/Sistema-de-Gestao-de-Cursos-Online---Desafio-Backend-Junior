from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Professor, Course, Student, Enrollment, Lesson
from .serializers import (
    ProfessorSerializer,
    CourseSerializer,
    StudentSerializer,
    EnrollmentSerializer,
    LessonSerializer
)

# API Views para operações de CRUD
class ProfessorViewSet(viewsets.ModelViewSet):
    """
    API para gerenciar Professores.
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API para gerenciar Cursos.
    """
    queryset = Course.objects.select_related('instructor').all()
    serializer_class = CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API para gerenciar Estudantes.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    API para gerenciar Matrículas.
    """
    queryset = Enrollment.objects.select_related('student', 'course').all()
    serializer_class = EnrollmentSerializer


class LessonViewSet(viewsets.ModelViewSet):
    """
    API para gerenciar Aulas.
    """
    queryset = Lesson.objects.select_related('course').all()
    serializer_class = LessonSerializer


# Views para renderização de templates
def homepage(request):
    """
    Página inicial com dados sobre cursos, professores, alunos e aulas.
    """
    # Busca os dados necessários do banco de dados
    courses = Course.objects.select_related('instructor').all()
    professors = Professor.objects.all()
    students = Student.objects.all()
    lessons = Lesson.objects.select_related('course').all()

    # Dados para renderização
    context = {
        'courses': courses,
        'professors': professors,
        'students': students,
        'lessons': lessons,
    }

    return render(request, 'homepage.html', context)


def course_detail(request, course_id):
    """
    Página de detalhes de um curso específico.
    """
    course = get_object_or_404(Course.objects.select_related('instructor'), pk=course_id)
    lessons = course.lessons.all()
    students = course.enrollments.select_related('student').all()

    context = {
        'course': course,
        'lessons': lessons,
        'students': students,
    }

    return render(request, 'courses/course_detail.html', context)


def professor_detail(request, professor_id):
    """
    Página de detalhes de um professor específico.
    """
    professor = get_object_or_404(Professor, pk=professor_id)
    courses = professor.courses.all()

    context = {
        'professor': professor,
        'courses': courses,
    }

    return render(request, 'courses/professor_detail.html', context)
