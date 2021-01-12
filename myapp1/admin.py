from django.contrib import admin
from .models import Student
from .models import StudentDetail
from .models import StudentFeesDetail
# Register your models here.
admin.site.register(Student)
admin.site.register(StudentFeesDetail)
admin.site.register(StudentDetail)