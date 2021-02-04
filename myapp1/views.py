from django.shortcuts import render, HttpResponse
from .models import Student,StudentDetail,Employee

# Create your views here.


def home(request):

    return render(request, 'index.html')

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
    return render(request, 'basic-form.html')
   

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

def update_student(request, slug):
    if request.method == "POST":
        stu_name = request.POST.get('name')
        print(stu_name)
        rollno = request.POST.get('rollnumber')
        
        obj = Student.objects.get(rollno = slug)
        obj.name = stu_name
        obj.rollno = rollno
        obj.save()
        # filter = [list of objects]
        # get = single object
        return HttpResponse("updated successfully")
    obj = Student.objects.filter(rollno = slug)
    return render(request, 'update-form.html', {"data":obj})


def add_detail(request):
    if request.method=='POST':
        name=request.POST.get('name')
        rollno=request.POST.get('rollno')
        email=request.POST.get('email')
        fname=request.POST.get('f_name')
        mname=request.POST.get('m_name')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        obj=StudentDetail(name=name,rollno=rollno,f_name=fname,m_name=mname,address=address,dateOfBirth=dob,stu_class='1' )
        obj.save()
        return HttpResponse('added successfully')
    return render(request,'basic-form.html')
def emp_details(request):
    if request.method=='POST':
        name=request.POST.get('name')
        emp_id=request.POST.get('e_Id')
        age=request.POST.get('e_age')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        email=request.POST.get('email')
        salary=request.POST.get('salary')
        obj=Employee(name=name,e_id=emp_id,age=age,gender=gender,address=address, salary=salary)
        obj.save()
        return HttpResponse('added successfully')
    return render(request,'emp-details.html')
def update_stu(request):
    if request.method=='POST':
        rollno=request.POST.get('rollnumber')
        obj=Student.objects.get(rollno)
        obj.rollno=rollno
        obj.save()
        return HttpResponse('data is updated successfully')
    return render(request,'basic-form.html')