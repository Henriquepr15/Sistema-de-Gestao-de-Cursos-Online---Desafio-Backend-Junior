from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Course, Professor

class CourseTestCase(TestCase):
    def setUp(self):
        self.professor = Professor.objects.create(name="João", email="joao@example.com")
        self.course = Course.objects.create(
            title="Django Basics",
            description="Learn Django step by step.",
            workload=40,
            instructor=self.professor
        )

    def test_course_creation(self):
        self.assertEqual(self.course.title, "Django Basics")
        self.assertEqual(self.course.workload, 40)

    def test_course_instructor(self):
        self.assertEqual(self.course.instructor.name, "João")
