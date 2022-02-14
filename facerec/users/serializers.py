from . import models
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id', 'name', 'email', 'phone', 'rollno', 'hostel')


class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    class Meta:
        model = models.Attendance
        fields = ('id', 'student', 'date', 'time', 'status')

class StudentPhotoSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    class Meta:
        model = models.StudentPhoto
        fields = ('id', 'student', 'photo')