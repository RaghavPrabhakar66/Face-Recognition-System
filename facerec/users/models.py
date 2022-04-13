from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return f'database/{instance.first_name}_{str(instance.id)}.{ext}'

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
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(default=0)
    is_outside = models.BooleanField(default=False)
    is_late = models.BooleanField(default=False)
    rollno = models.IntegerField(default=0)
    hostel = models.CharField(max_length=200, choices=HOSTEL)
    video = models.FileField(upload_to=upload_path)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def isOutside(self):
        a = Attendance.objects.filter(student=self).order_by('-id')[0]
        if a.status == 'exit':
            self.isOutside = True
            return
        
        self.isOutside = False
        return


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

@receiver(post_save, sender=Attendance, dispatch_uid="my_unique_identifier")
def update_outside_field(sender, instance, **kwargs):
    status = instance.status
    if status == 'exit':
        instance.student.is_outside = True
    else:
        instance.student.is_outside = False
    
    instance.student.save()
    

class User(AbstractUser):
    email = models.EmailField(unique=True)
    hostel = models.CharField(max_length=200, choices=Student.HOSTEL)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'hostel']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email