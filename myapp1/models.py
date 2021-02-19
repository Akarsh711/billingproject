from django.db import models

class Course(models.Model):
    course_name=models.CharField(max_length = 23)

    def __str__(self):
        return self.course_name


class Branch(models.Model):
    branch_name=models.CharField(max_length=30)
    course_name=models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):

        return self.branch_name

class BranchFees(models.Model):
    fees=models.IntegerField(null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

class StudentFeesDetail(models.Model):
    tutionFee=models.ForeignKey(Course,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete = models.CASCADE, null=True)
    maintenanceCharges1=models.IntegerField(null=True)
    examFee=models.IntegerField(null=True)
    libraryCharges=models.IntegerField(null=True)
    totalFee=models.IntegerField()
    pay_date=models.DateTimeField()
    
    def __str__(self):
        return f'this is id - {self.id}'
    


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 23)
    rollno = models.IntegerField()
    stu_class = models.CharField(max_length = 23)
    f_name= models.CharField(max_length = 23)
    m_name= models.CharField(max_length = 23)
    dateOfBirth = models.DateTimeField()
    address = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    fees = models.ForeignKey(StudentFeesDetail, on_delete=models.CASCADE)
        
    def __str__(self):
        return f'rollno:{self.rollno}'
    


#class StudentDetail(models.Model):
  

    #fees = models.ForeignKey(StudentFeesDetail, on_delete=models.CASCADE)
class Employee(models.Model):
    name=models.CharField(max_length=25)
    e_id=models.IntegerField()
    gender=models.CharField(max_length=10)
    age=models.CharField(max_length=25)
    address=models.CharField(max_length=25)
    #dob=models.DateTimeField()
    salary=models.CharField(max_length=25)
   # email=models.CharField(max_length=25)
    

    
    

    