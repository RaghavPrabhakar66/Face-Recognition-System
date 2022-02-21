from . import models
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer

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

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'password', 'hostel', 'first_name', 'last_name')