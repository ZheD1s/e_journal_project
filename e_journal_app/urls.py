from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('cabinet/', cabinetView, name='cabinet'),
    path('group_student/<int:group_id>', groupStudentView, name='group_student'),
    path('t_subjects/', lessonsView, name='my_subjects'),
    path('student_cabinet/', studentCabinetView, name='student_cabinet'),
    path('groups/', groupsView, name='groups'),
    path('students/', allStudentsListView, name='all_students'),
    path('', homeView, name='home'),
]