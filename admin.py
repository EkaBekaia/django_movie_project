from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Course, Lecturer

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Lecturer)
