from django.contrib import admin
#from .models import Student
#from .models import StudentDetail
#from .models import StudentFeesDetail
#from.models import studentCourse
from .models import*
# Register your models here.
admin.site.register(Student)
admin.site.register(StudentFeesDetail)
admin.site.register(StudentDetail)
admin.site.register(studentCourse)
admin.site.register(Employee)