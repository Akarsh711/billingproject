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

# CRUD [Create ,Retrive, Update, Delete]--------------

# Create/Data Add karna
def add_student(request):
    if request.method == 'POST':

        stu_name = request.POST.get('name')
        stu_roll = request.POST.get('rollnumber')

        obj = Student(name = stu_name, rollno = stu_roll)
        obj.save()

        return HttpResponse(f'stu_roll:{stu_roll}')
    return render(request, 'add-student.html')
   

# RETRIVE
def student_detail(request, slug):
    obj = Student.objects.filter(rollno = slug)
    # obj = [obj1, obj2]
    # temp = obj[0]
    # temp.rollno
    # temp.name
    tam = obj[0]

    return HttpResponse(f'rollno:{tam.rollno}, name:{tam.name}this is slug -{slug}')

def delete_student(request):
    if request.method == 'POST':

        stu_rollno = request.POST.get('rollnumber')
        obj = Student.objects.filter(rollno = stu_rollno)
        obj.delete()
        return HttpResponse('User Deleted Successfully sayad')
    return render(request, 'delete-student.html')