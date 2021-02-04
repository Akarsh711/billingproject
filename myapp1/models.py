from django.db import models

class studentCourse(models.Model):
    course=models.CharField(max_length = 23)
    fees=models.IntegerField()
    


# Create your models here.
class Student(models.Model):
    # id = models.IntgerField(primary_key = True) 
    name = models.CharField(max_length = 23)
    rollno = models.IntegerField()
    
    
    
    def __str__(self):
        return f'rollno:{self.rollno}'
    
class StudentFeesDetail(models.Model):
    tutionFee=models.ForeignKey(studentCourse,on_delete=models.CASCADE)
    maintenanceCharges1=models.IntegerField(null=True)
    examFee=models.IntegerField(null=True)
    libraryCharges=models.IntegerField(null=True)
    totalFee=models.IntegerField()
    pay_date=models.DateTimeField()
    
    def __str__(self):
        return f'this is id - {self.id}'
    

class StudentDetail(models.Model):
    name = models.CharField(max_length = 23)
    rollno = models.IntegerField()
    stu_class = models.CharField(max_length = 23)
    f_name= models.CharField(max_length = 23)
    m_name= models.CharField(max_length = 23)
    dateOfBirth = models.DateTimeField()
    address = models.TextField()

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
    

    
    

    