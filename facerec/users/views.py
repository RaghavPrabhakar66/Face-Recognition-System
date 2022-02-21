from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
from . import models
from . import serializers
from rest_framework import generics

class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class AttendanceList(generics.ListCreateAPIView):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer


class StudentPhotoList(generics.ListCreateAPIView):
    queryset = models.StudentPhoto.objects.all()
    serializer_class = serializers.StudentPhotoSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restrcited(request, *args, **kwargs):
    return Response(data="You are authorized to access this page", status=status.HTTP_200_OK)