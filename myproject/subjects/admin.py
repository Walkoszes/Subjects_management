from django.contrib import admin
from .models import Subject, Teacher, Class, Student
# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "subject")
    list_filter = ("subject",)
    search_fields = ("name", "subject_name")

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "student_class")
    list_filter = ("student_class",)
    search_fields = ("name", "student_class_name")