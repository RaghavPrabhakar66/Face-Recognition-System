from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import status

from . import models
from . import serializers

class StudentList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = models.Student.objects.all()
        first_name = self.request.data.get('first_name', None)
        if first_name is not None:
            queryset = queryset.filter(first_name=first_name)
        return queryset

    serializer_class = serializers.StudentSerializer

class StudentActions(generics.RetrieveUpdateDestroyAPIView):
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