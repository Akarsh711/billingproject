from django.contrib import admin
from django.urls import path, include
from employee import views

urlpatterns = [
	path('add_employee', views.add_employee, name='add-employee'),
	path('r_update_employee', views.r_update_employee, name='r-update-employee'),
	path('update_employee', views.update_employee, name='update-employee'),

	path('add_department', views.add_department, name='add-department'),
	path('department_list', views.department_list, name='department-list'),
	path('delete_department/<int:slug>', views.delete_department, name='delete-department'),

	path('emp_search', views.emp_search, name='emp-search'),
	path('pay_salary', views.pay_salary, name='pay-salary'),
]
