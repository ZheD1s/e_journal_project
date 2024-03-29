from django.shortcuts import render, redirect
from django.views.generic import DeleteView, DetailView
from django.urls import reverse_lazy
from .models import *

# Create your views here.

def homeView(request):
    thisUser = request.user
    try:
        thisStudent = Student.objects.get(user_id=thisUser) # Get data from table Student
        thisUserType = 'Student'
        subjects = Subject.objects.all()  # get data from table Subject
        return render(request,
                      template_name='home.html',
                      context={
                          'type': thisUserType,
                          'subjects': subjects
                      })  # context - datas to show on template
    except:
        thisUserType = 'Teacher'
        thisTeacher = Teacher.objects.get(user_id=request.user)
        subjects = thisTeacher.subject
        return render(request,
                      template_name='home.html',
                      context={
                          'type': thisUserType,
                          'subjects': subjects
                      })  # context - datas to show on template

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

def groupStudentView(request, group_id):
    query = Student.objects.filter(group=Group.objects.get(id=group_id))
    return render(request,
                  'group_student.html',
                  context={
                      'students': query,
                  })


def allStudentsListView(request):
    students = Student.objects.all()
    return render(request,
                  'students.html',
                  context={
                      'students': students,
                  })

def changeStudentView(request):
    if request.method == 'POST':
        thisStudent = Student.objects.get(user_id=request.user)
        thisStudent.name = request.POST.get('name_input')
        thisStudent.surname = request.POST.get('surname_input')
        thisStudent.save()
        return redirect('student_cabinet')
    else:
        return render(request,
                      'student_change.html',
                      context={
                          'student': Student.objects.get(user_id=request.user),
                      })

def teacherAddSubjectView(request):
    if request.method == 'POST':
        try:
            subject_id = int(request.POST.get('subjects'))
            new_subject = Subject.objects.get(id=int(subject_id))
            thisTeacher = Teacher.objects.get(user_id=request.user)
            thisTeacher.subject.add(new_subject)
            thisTeacher.save()
            return redirect('home')
        except TypeError:
            return redirect('add_subjects')
    else:
        teachersSubjects = set(Teacher.objects.get(user_id=request.user).subject.all())
        allSubjects = set(Subject.objects.all())
        newSubjects = allSubjects.difference(teachersSubjects)
        return render(request,
                      'add_subject.html',
                      context={
                          'new_subjects': newSubjects
                      })

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subject_detail.html'
    context_object_name = 'subject_detail'

class subjectDeleteView(DeleteView):
    model = Subject
    template_name = 'subject_delete.html'
    success_url = reverse_lazy('home')
