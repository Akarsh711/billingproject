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
    tution_fees = models.IntegerField(null=True)
    exam_fees = models.IntegerField(null=True)
    library_charges = models.IntegerField(null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


class Student(models.Model):
    name = models.CharField(max_length = 23)
    rollno = models.IntegerField(unique=True)
    email = models.CharField(max_length = 23)
    stu_class = models.CharField(max_length = 23)
    f_name= models.CharField(max_length = 23)
    m_name= models.CharField(max_length = 23)
    dateOfBirth = models.DateTimeField()
    address = models.TextField()
    # course = models.ForeignKey(Course,  on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    # fees = models.ForeignKey(StudentFeesDetail, on_delete=models.CASCADE)
        
    def __str__(self):
        return f'rollno:{self.rollno}'
    


class PaidFees(models.Model):

    # name =models.CharField(max_length=45)   
    # rollno =models.IntegerField(null=True)
    # f_name =models.CharField(max_length=45)
    # dob = models.DateTimeField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_fee = models.IntegerField(null=False)
    tution_fee=models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete = models.CASCADE, null=True)
    exam_fee=models.IntegerField(null=True)
    library_charges=models.IntegerField(null=True)
    total_fee=models.IntegerField()
    pay_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'this is id - {self.id}'
    
# class StudentDetail(models.Model):
#     name = models.CharField(max_length = 23)
#     rollno = models.IntegerField()
#     stu_class = models.CharField(max_length = 23)
#     f_name= models.CharField(max_length = 23)
#     m_name= models.CharField(max_length = 23)
#     dateOfBirth = models.DateTimeField()
#     address = models.TextField()





class Employee(models.Model):
    name=models.CharField(max_length=25)
    e_id=models.IntegerField()
    gender=models.CharField(max_length=10)
    age=models.CharField(max_length=25)
    address=models.CharField(max_length=25)
    #dob=models.DateTimeField()
    salary=models.CharField(max_length=25)
   # email=models.CharField(max_length=25)
    

    
    

    