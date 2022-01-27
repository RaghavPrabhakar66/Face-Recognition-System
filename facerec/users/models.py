from django.db import models
import uuid

# Create your models here.
class Profile(models.Model):

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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    rollno = models.IntegerField(default=0)
    hostel = models.CharField(max_length=200, choices=HOSTEL)


class Attendance(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=200, default='Absent')

    def __str__(self):
        return self.student.name

