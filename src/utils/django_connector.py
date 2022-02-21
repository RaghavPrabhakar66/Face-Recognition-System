import requests

def get_user_id(name):
    student_url = 'http://localhost:8000/api/students'
    student_details = requests.get(student_url, data={'name': name}, auth=('a@a.com', 'admin'))
    # get id from json data
    # print(student_details.json()[0]['id'])
    return student_details.json()[0]['id']


def add_attendance(name):
    student_id = get_user_id(name)
    attendance_url = 'http://localhost:8000/api/attendances'
    attendance_details = requests.post(attendance_url, data={'student_id': student_id}, auth=('a@a.com', 'admin'), headers={"Authorization": "Token 7b49e4ab9c734b0db015fe9eb3411652ffb9f8ce"})
    # print(attendance_details)

add_attendance("Shivang")