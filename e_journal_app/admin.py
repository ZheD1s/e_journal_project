from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Group)
admin.site.register(Grade)
admin.site.register(Exams)
admin.site.register(Teacher)
admin.site.register(Attendance)
admin.site.register(Subject)



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'group', 'average_grade')

    class Meta:
        ordering = ('surname', 'name')
        # sorting by fields

    def average_grade(self, obj):
        from django.db.models import Avg
        result = Grade.objects.filter(student=obj).aggregate(Avg('points'))
        return result['points__avg']