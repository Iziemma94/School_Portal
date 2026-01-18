# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.username} ({self.role})"

class Class(models.Model):
    name = models.CharField(max_length=50)
    school_level = models.CharField(max_length=20, choices=[("Primary","Primary"),("Secondary","Secondary")])

class Subject(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    classes = models.ManyToManyField(Class)

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mid_term_score = models.DecimalField(max_digits=5, decimal_places=2)
    exam_score = models.DecimalField(max_digits=5, decimal_places=2)
    term = models.CharField(max_length=20)
    year = models.IntegerField()

    @property
    def total_score(self):
        return self.mid_term_score + self.exam_score

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def outstanding(self):
        return self.total_amount - self.amount_paid

class Note(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file = models.FileField(upload_to='notes/')
    student_group = models.ForeignKey(Class, on_delete=models.CASCADE)

class ReportCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.CharField(max_length=20)
    year = models.IntegerField()
    class_teacher_remark = models.TextField(blank=True, null=True)
    head_teacher_remark = models.TextField(blank=True, null=True)