from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from .models import *

# TODO
	# Check Cruds
def add_employee(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		f_name = request.POST.get('f_name')
		dob = request.POST.get('dob')
		department_id = request.POST.get('Department')
		print('..........', department_id)
		designation = request.POST.get('designation')
		salary = request.POST.get('salary')
		address = request.POST.get('address')
		department = Department.objects.filter(id=department_id).first()
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
		obj =Department.objects.all()
		return render(request, 'employee-form.html', {'departments':obj})
	obj =Department.objects.all()
	return render(request, 'employee-form.html', {'departments':obj})


def r_update_employee(request):
	if request.method == 'POST':
		emp_id = request.POST.get('search')
		obj =Department.objects.all()
		emp = Employee.objects.filter(employee_id = emp_id).first
		return render(request, 'employee-update-form.html', {'departments':obj, 'emp':emp})


def update_employee(request):
	if request.method == 'POST':
		emp_id = request.POST.get('id')
		name = request.POST.get('name')
		f_name = request.POST.get('f_name')
		dob = request.POST.get('dob')
		department_id = request.POST.get('Department')
		print('..........', department_id)
		designation = request.POST.get('designation')
		salary = request.POST.get('salary')
		address = request.POST.get('address')
		department = Department.objects.filter(id=department_id).first()
		emp = Employee.objects.filter(employee_id = emp_id).first()
		emp.name = name
		emp.f_name = f_name
		emp.dob = dob
		emp.department = department
		emp.designation = designation
		emp.salary = salary
		emp.address = address
		emp.save()
		messages.success(request, 'Employee Updated Successfully!')
		obj =Department.objects.all()
		return render(request, 'employee-update-form.html', {'departments':obj})
	return HttpResponse('Invalid Request')


def add_department(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		Department.objects.all()
		obj = Department()
		obj.name = name
		obj.save()
		messages.success(request, 'added successfully')
		return render(request, 'department-form.html')
	return render(request, 'department-form.html')

def department_list(request):
	obj = Department.objects.all()
	return render(request, 'department-list.html', {'departments':obj})

def delete_department(request, slug):
	Department.objects.filter(id = slug).delete()
	return redirect('department-list')

def emp_search(request):
	if request.method == 'POST':
		emp_id = request.POST.get('id')
		emp = Employee.objects.filter(employee_id = emp_id).first()
		if emp == None:
			messages.error(request, 'Employee Not Found')
			return render(request, 'emp-search-form.html')
		return render(request, 'emp-salary-form.html', {'emp':emp})
	return render(request, 'emp-search-form.html')

def pay_salary(request):
	if request.method =='POST':
		emp_id = request.POST.get('id')
		name = request.POST.get('name')
		f_name = request.POST.get('f_name')
		dob = request.POST.get('dob')
		department = request.POST.get('Department')
		print('.........')
		designation = request.POST.get('designation')
		salary = request.POST.get('salary')
		emp = Employee.objects.filter(employee_id = emp_id).first()
		obj = Salaries()
		obj.employee = emp
		obj.name =name
		obj.f_name = f_name
		obj.department = department
		obj.designation = designation
		obj.salary = salary
		obj.save()
		messages.success(request, 'Salary paid Successfully')
		return render(request, 'emp-search-form.html')
	return HttpResponse('Invalid Request')