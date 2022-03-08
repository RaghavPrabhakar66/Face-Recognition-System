from . import models
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'rollno', 'hostel')

class AttendanceSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(source='student.id', write_only=True)
    student = StudentSerializer(read_only=True)
    class Meta:
        model = models.Attendance
        fields = ('id', 'student_id', 'student', 'date', 'time', 'status')

    def create(self, validated_data):
        student_data = validated_data.pop('student')
        student = models.Student.objects.get(id=student_data['id'])
        attendance = models.Attendance.objects.create(student=student, **validated_data)
        return attendance

class StudentPhotoSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    class Meta:
        model = models.StudentPhoto
        fields = ('id', 'student', 'photo')

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'password', 'hostel', 'first_name', 'last_name')