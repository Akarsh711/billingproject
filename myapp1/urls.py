# def update_course(request):
#     return render(request, 'course-form.html')

# def add_course(request):
#     return render(request, 'course-form.html')

# def add_branch(request):
#     return render(request, 'branch-form.html')

# def update_branch(request):
#     return render(request, 'branch-form.html')

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('',views.home),
	path('add_course', views.add_course, name='add-course'),
	path('add_branch', views.add_branch, name='add-branch'),
	path('add_course_detail', views.add_course_detail, name='add-course-detail'),
	path('r_update_course', views.render_update_branch, name='r-update-course'),
	path('update_course', views.update_course, name='update-course'),
	path('add_branch', views.add_branch, name='add-branch'),
	path('update_branch', views.update_branch, name='update-branch'),
	path('branch_search', views.branch_search, name='branch-search'),
]