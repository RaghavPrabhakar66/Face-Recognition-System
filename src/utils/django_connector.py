import requests

def django_data(name):
    student_url = 'http://localhost:8000/api/students'
    student_details = requests.get(student_url, data={'name': name}, auth=('admin@admin.com', 'admin'))
    # get id from json data
    return student_details.json()[0]['id']


def add_attendance(name):
    student_id = django_data(name)
    attendance_url = 'http://localhost:8000/api/attendances'
    attendance_details = requests.post(attendance_url, data={'student': student_id}, auth=('admin@admin.com', 'admin'))
    print(attendance_details.status_code)

add_attendance('Sanchit')