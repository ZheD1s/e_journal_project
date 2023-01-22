from django.shortcuts import render
from .models import *

# Create your views here.

def homeView(request):
    thisUser = request.user
    subjects = Subject.objects.all() # get data from table Subject
    try:
        thisStudent = Student.objects.get(user_id=thisUser) # Get data from table Student
        thisUserType = 'Student'
    except:
        thisUserType = 'Teacher'
    return render(request,
                  template_name='home.html',
                  context={
                      'type': thisUserType,
                      'subjects': subjects
                  }) # context - datas to show on template

def lessonsView(request):
    thisUser = request.user
    all_subjects = Teacher.objects.get(user_id=thisUser).subject.all()
    return render(request,
            template_name='my_subjects.html',
            context={
                'subjects': all_subjects
            })