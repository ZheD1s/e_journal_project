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
    list_filter = ('group',)
    search_fields = ('surname__startswith',)
    class Meta:
        ordering = ('surname', 'name')
        # sorting by fields


    def average_grade(self, obj):
        from django.db.models import Avg
        from django.utils.html import format_html
        result = Grade.objects.filter(student=obj).aggregate(Avg('points'))
        return format_html('<b>{}</b>', result['points__avg'])