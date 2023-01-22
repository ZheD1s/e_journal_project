from django.shortcuts import render
from .models import *

# Create your views here.

def homeView(request):
    thisUser = request.user
    try:
        thisStudent = Student.objects.get(user_id=thisUser) # Get data from table Student
        thisUserType = 'Student'
    except:
        thisUserType = 'Teacher'
    return render(request,
                  template_name='home.html',
                  context={
                      'type': thisUserType
                  }) # context - datas to show on template