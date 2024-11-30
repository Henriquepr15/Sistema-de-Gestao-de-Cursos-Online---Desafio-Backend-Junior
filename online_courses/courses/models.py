from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
from django.db import models

class Professor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    workload = models.PositiveIntegerField()  # Carga horária em horas
    instructor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title

    def clean(self):
        if self.workload <= 0:
            raise ValidationError("A carga horária deve ser maior que zero.")
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    topic = models.CharField(max_length=200)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.topic} ({self.date_time})"
