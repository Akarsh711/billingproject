from django.db import models

# Create your models here.
class Department(models.Model):
	name = models.CharField(max_length=50)

class Employee(models.Model):
	employee_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=23)
	f_name = models.CharField(max_length=23)
	dob = models.CharField(max_length=11)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	designation = models.CharField(max_length=50)
	salary = models.IntegerField()
	address = models.TextField()

class Salaries(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	name = models.CharField(max_length=23)
	f_name = models.CharField(max_length=23)
	department = models.CharField(max_length = 50)
	designation = models.CharField(max_length=50)
	salary = models.IntegerField()
	transaction_date = models.DateTimeField(auto_now_add=True)