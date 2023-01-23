from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('t_subjects/', lessonsView, name='my_subjects'),
    path('student_cabinet/', studentCabinetView, name='student_cabinet'),
    path('', homeView, name='home'),
]