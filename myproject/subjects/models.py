from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name