from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Grade)
admin.site.register(Exams)
admin.site.register(Attendance)



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


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name','admission_year')
    list_filter = ('admission_year',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ('surname__startswith',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_kzt')
    def price_kzt(self, obj):
        result = Subject.objects.filter(title=obj).first()
        if result is not None:
            result = result.price * 22000
        return str(result) + ' KZT'
# Только в Админке. В модели не лезть
# Добавить колонку в Subject price но в kzt
# Счиать что 1 кредит в Price равен 22000 KZT