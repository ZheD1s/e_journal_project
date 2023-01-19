from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Exams)
admin.site.register(Teacher)
admin.site.register(Attendance)