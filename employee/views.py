from django.shortcuts import render
from django.contrib import messages
from .models import *

# Create your views here.
def add_employee(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		f_name = request.POST.get('f_name')
		dob = request.POST.get('dob')
		department = request.POST.get('Department')
		designation = request.POST.get('designation')
		salary = request.POST.get('salary')
		address = request.POST.get('address')
		emp = Employee() 
		emp.name = name
		emp.f_name = f_name
		emp.dob = dob
		emp.department = department
		emp.designation = designation
		emp.salary = salary
		emp.address = address
		emp.save()
		messages.success(request, 'Employee Added Successfully!')
	return render(request, 'employee-form.html')

def add_department(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		Department(name =name).save()
		messages.success(request, 'added successfully')
		return render(request, 'department-form.html')
	return render(request, 'department-form.html')