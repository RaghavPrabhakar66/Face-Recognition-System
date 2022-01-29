from django.shortcuts import render

# Create your views here.
from . import models
from . import serializers
from rest_framework import generics

class ProfileList(generics.ListAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class AttendanceList(generics.ListAPIView):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer


class StudentPhotoList(generics.ListAPIView):
    queryset = models.StudentPhoto.objects.all()
    serializer_class = serializers.StudentPhotoSerializer