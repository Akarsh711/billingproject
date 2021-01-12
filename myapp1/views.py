from django.shortcuts import render, HttpResponse
from .models import Student
# Create your views here.



def home(request):
    obj = Student.objects.all()
    obj = obj[2]
    name = obj.name
    obj2 = dir(obj)
    return render(request, 'tam.html', {'tamobj':name})

def form(request):
    name = request.POST.get('name1')
    rollno = request.POST.get('pswd')
    obj = Student(name=name , rollno=rollno)
    obj.save()
    return HttpResponse('ye walla function hit hua hai')