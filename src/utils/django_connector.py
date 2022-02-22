import requests

def get_user_id(name, creds):
    student_url = 'http://localhost:8080/api/students'
    student_details = requests.get(student_url, data={'name': name}, auth=(creds[0], creds[1]))
    # get id from json data
    # print(student_details.json()[0]['id'])
    return student_details.json()[0]['id']

def add_attendance(name, creds):
    student_id = get_user_id(name)
    attendance_url = 'http://localhost:8080/api/attendances'
    attendance_details = requests.post(attendance_url, data={'student_id': student_id}, auth=(creds[0], creds[1]), headers={"Authorization": "Token " + creds[2]})
    # print(attendance_details)

def login(creds):
    res = requests.post("http://localhost:8080/auth/token/login", data={'password': creds[1], 'email': creds[0]})
    creds.append(res.json()['auth_token'])
    return creds