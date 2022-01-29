from . import models
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ('id', 'name', 'email', 'phone', 'rollno', 'hostel')


class AttendanceSerializer(serializers.ModelSerializer):
    student = ProfileSerializer(read_only=True)
    class Meta:
        model = models.Attendance
        fields = ('id', 'student', 'date', 'time', 'status')

class StudentPhotoSerializer(serializers.ModelSerializer):
    student = ProfileSerializer(read_only=True)
    class Meta:
        model = models.StudentPhoto
        fields = ('id', 'student', 'photo')