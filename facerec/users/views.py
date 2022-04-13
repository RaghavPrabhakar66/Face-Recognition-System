from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import status
import csv
from django.http import HttpResponse

from . import models
from . import serializers
import datetime

class StudentList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = models.Student.objects.filter(hostel=self.request.user.hostel)
        first_name = self.request.data.get('first_name', None)
        if first_name is not None:
            queryset = queryset.filter(first_name=first_name)
        return queryset

    parser_classes = [MultiPartParser, FormParser]
    serializer_class = serializers.StudentSerializer

class StudentActions(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = serializers.StudentSerializer


class AttendanceList(generics.ListCreateAPIView):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer

# debug
@api_view(['GET'])
def missing_students_csv(request):
    response = HttpResponse(content_type='text/csv')
    filename = f'missing_students_{datetime.datetime.now().date()}.csv'
    response['Content-Disposition'] = f'attachment; filename={filename}'

    writer = csv.writer(response)
    writer.writerow(['Status', 'First name', 'Last name', 'Roll no.', 'Phone no.', 'Email Address'])

    try:
        students = models.Student.objects.filter(is_late=True).values_list('first_name', 'last_name', 'rollno', 'phone', 'email')
        print(students)
        for student in students:
            student = list(student)
            student.insert(0, 'Late')
            writer.writerow(student)
    except:
        print("No students late")


    try:
        students = models.Student.objects.filter(is_outside=True).values_list('first_name', 'last_name', 'rollno', 'phone', 'email')
        for student in students:
            student = list(student)
            student.insert(0, 'Missing')
            writer.writerow(student)
    except:
        print("No students missing")

    return response