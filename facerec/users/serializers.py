from . import models
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as UserCreate


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(source='student.id', write_only=True)
    student = StudentSerializer(read_only=True)
    class Meta:
        model = models.Attendance
        fields = '__all__'

    def create(self, validated_data):
        student_data = validated_data.pop('student')
        student = models.Student.objects.get(id=student_data['id'])
        attendance = models.Attendance.objects.create(student=student, **validated_data)
        return attendance

class UserCreateSerializer(UserCreate):
    class Meta(UserCreate.Meta):
        model = models.User
        fields = ('id', 'email', 'password', 'hostel', 'first_name', 'last_name')