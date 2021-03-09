"""billingproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp1 import views

urlpatterns = [
    path('tadmin/', admin.site.urls),
    path('', include('myapp1.urls')),
    path('emp/', include('employee.urls')),
    path('form', views.form),

    # CRUD
    path('student_detail/<str:slug>',views.student_detail),
    path('add_student2', views.add_student),
    # path('delete_student', views.delete_student),
    path('delete_student/<int:slug>', views.delete_student, name='delete-student'),
    path('update_student/<str:slug>', views.update_student),
    path('update_stu_with_rollno', views.update_stu_with_rollno, name='update-stu-with-rollno'),
    path('add_student',views.add_detail),
    path('emp_detail',views.emp_details),
    path('update2_stu',views.update_stu, name='update-stu'),
    path('update3',views.update3),
    path('userlogin',views.loginuser, name='user-login'),
    path('logoutuser',views.logoutuser, name='logout'),

    # Fees Pay Urls
    path('fees_form' ,views.fees_form, name='fees-form'),
    path('fees_form/<int:slug>', views.fees_form_with_rollno, name='fees-form-rollno'),
    path('pay_fees', views.pay_fees),
]
