from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    admission_year = models.DateField(null=False, blank=False)


class Student(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE) # Only One student to One User
    name = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    group = models.ForeignKey('Group', on_delete=models.CASCADE) # Many students can have One group

class Subject(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    price = models.PositiveSmallIntegerField()

class Grade(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    points = models.PositiveSmallIntegerField(null=False, blank=False)
    week = models.PositiveSmallIntegerField(null=False, blank=False)
    semester = models.PositiveSmallIntegerField(null=False, blank=False)

class Exams(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    points = models.PositiveSmallIntegerField(null=False, blank=False)
    type = models.CharField(max_length=10, choices=[
        ('RK1', 'Рубежный контроль 1'),
        ('RK2', 'Рубежный контроль 2'),
        ('Session', 'Финальный экзамен')
    ])

class Teacher(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)  # Only One student to One User
    name = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    subject = models.ManyToManyField('Subject') # Many teachers can have Many subjects

class Attendance(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, auto_now_add=True)
    attended = models.BooleanField(null=False, blank=False, default=True)