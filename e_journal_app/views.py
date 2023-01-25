from django.shortcuts import render, redirect
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

def studentCabinetView(request):
    thisStudent = Student.objects.get(user_id=request.user)
    thisGrades = Grade.objects.filter(student=thisStudent)
    # filter - get many records from table with (student=thisStudent) condition
    return render(request,
                  'student_cabinet.html',
                  context={
                      'student': thisStudent,
                      'grades': thisGrades
                  })

def cabinetView(request):
    try:
        Student.objects.get(user_id=request.user)
        return redirect('student_cabinet')
    except:
        return redirect('home')

def groupsView(request):
    all_groups = Group.objects.all()
    return render(request,
                  'groups.html',
                  context={
                      'groups': all_groups,
                  })

def groupStudentView(request):
    all_student = Student.objects.all()
    return render(request,
                  'group_student.html',
                  context={
                      'students': all_student,
                  })


