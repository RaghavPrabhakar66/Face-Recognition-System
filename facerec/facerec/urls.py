"""facerec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from users.views import StudentList, AttendanceList, StudentPhotoList, StudentActions, missing_students_csv

admin.site.site_header = "Hostel Facial Recognition"
admin.site.site_title = "Capstone Project"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students', StudentList.as_view(), name='student'),
    path('api/student-actions/<int:pk>', StudentActions.as_view(), name='student-actions'),
    path('api/attendances', AttendanceList.as_view(), name='attendance'),
    path('api/images', StudentPhotoList.as_view(), name='images'), # remove
    path('auth/', include('users.urls')),
    path('api/export/csv', missing_students_csv, name='missing_students_csv'),
    re_path(r'^(?:.*)/?$', include('frontend.urls')),
]
