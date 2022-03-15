import datetime
from django.utils import timezone
import email
from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.

# def photo_upload_path(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = "%s.%s" % (uuid.uuid4(), ext)
#     return 'photos/{0}{1}/{2}'.format(instance.student.first_name, instance.student.last_name, filename)

def photo_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return f'database/{instance.student.first_name + str(instance.id)}.jpg'
   
class Student(models.Model):

    HOSTEL = (
        ('Hostel A', 'Hostel A'),
        ('Hostel B', 'Hostel B'),
        ('Hostel C', 'Hostel C'),
        ('Hostel D', 'Hostel D'),
        ('Hostel E', 'Hostel E'),
        ('Hostel F', 'Hostel F'),
        ('Hostel G', 'Hostel G'),
        ('Hostel H', 'Hostel H'),
        ('Hostel I', 'Hostel I'),
        ('Hostel J', 'Hostel J'),
        ('Hostel K', 'Hostel K'),
        ('Hostel L', 'Hostel L'),
        ('Hostel M', 'Hostel M'),
        ('Hostel N', 'Hostel N'),
        ('Hostel O', 'Hostel O'),
    )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(default=0)
    rollno = models.IntegerField(default=0)
    hostel = models.CharField(max_length=200, choices=HOSTEL)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def isOutside(self):
        a = Attendance.objects.filter(student=self).order_by('-id')[0]
        if a.status == 'exit':
            return True
        
        return False

    
class StudentPhoto(models.Model):
    student = models.ForeignKey(Student, related_name='photos',  on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=photo_upload_path)

    def __str__(self):
        return self.student.first_name + str(self.id)


class Attendance(models.Model):

    choices = (
        ('entry', 'Entry'),
        ('exit', 'Exit'),
    )

    student = models.ForeignKey(Student, related_name='student', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=choices)

    def __str__(self):
        return f"{self.student.first_name} : {self.date} : {self.time}"

class User(AbstractUser):
    email = models.EmailField(unique=True)
    hostel = models.CharField(max_length=200, choices=Student.HOSTEL)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'hostel']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email