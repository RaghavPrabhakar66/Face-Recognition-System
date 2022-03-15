from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :

from . import models

class StudentPhotoInline(admin.TabularInline):
    model = models.StudentPhoto
    extra = 3


class StudentAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'email', 'rollno', 'hostel')
    list_filter = ('id', 'first_name', 'last_name', 'email', 'rollno', 'hostel')
    search_fields = ('name',)
    inlines = [StudentPhotoInline,]


class AttendanceAdmin(admin.ModelAdmin):

    list_display = ('id', 'student', 'date', 'time', 'status')
    list_filter = (
        'student',
        'date',
        'id',
        'student',
        'date',
        'time',
        'status',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Student, StudentAdmin)
_register(models.User, admin.ModelAdmin)
_register(models.Attendance, AttendanceAdmin)
