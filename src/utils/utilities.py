import os
from datetime import datetime
# import cv2
import requests

def get_user_id(name, creds):
    student_url = 'http://localhost:8080/api/students'
    student_details = requests.get(student_url, data={'first_name': name}, auth=(creds[0], creds[1]))
    # get id from json data
    #print(student_details.json())
    for i in student_details.json():
        if i['first_name'] == name:
            print(i)
            return i['id']
    #return student_details.json()[0]['id']

def add_attendance(name, creds):
    student_id = get_user_id(name, creds)
    attendance_url = 'http://localhost:8080/api/attendances'
    attendance_details = requests.post(attendance_url, data={'student_id': student_id}, auth=(creds[0], creds[1]), headers={"Authorization": "Token " + creds[2]})
    # print(attendance_details)

def login(creds):
    res = requests.post("http://localhost:8080/auth/token/login", data={'password': creds[1], 'email': creds[0]})
    creds.append(res.json()['auth_token'])
    return creds

def facial_extraction(image, bbox, padding, size=(256, 256)):
    x, y, _, _ = bbox
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x, y, w, h = round(x), round(y), round(w), round(h)

    start_y, end_y = y - padding, y + h + padding
    start_x, end_x = x - padding, x + w + padding
    if start_y < 0:
        start_y = 0
    if end_y > image.shape[0]:
        end_y = image.shape[0]
    if start_x < 0:
        start_x = 0
    if end_x > image.shape[1]:
        end_x = image.shape[1]

    ratio = image.shape[1] // image.shape[0]
    try:
        face = cv2.resize(
            image[start_y:end_y, start_x:end_x], (size[0], ratio * size[0])
        )
    except:
        face = cv2.resize(image, (size[0], ratio * size[0]))

    return face, (size[0], ratio * size[0])

def record(name, creds):
    filepath = 'data/records/' + str(datetime.now().strftime('%d-%B-%Y'))
    try:    
        f = open(filepath + '/records.csv', 'x')
        f.close()
    except:
        pass
    os.makedirs(filepath, exist_ok=True)
    with open(filepath + '/records.csv', 'r+') as f:
        lines = f.readlines()
        records = [line.split(',')[0] for line in lines]
        if name not in records:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'{name},{time},{date}\n')
            add_attendance(name, creds)

def load_database(path):
    names = os.listdir(path)
    database = []
    
    for name in names:
        img = cv2.imread(f'{path}/{name}')
        database.append((os.path.splitext(name)[0], img))
    return database

creds = login(["a@a.com", "admin"])
# add_attendance("Shivang", creds)
# add_attendance("Kabir", creds)
# add_attendance("Shivang", creds)
# add_attendance("Sanchit", creds)
# add_attendance("Sanchit", creds)
# add_attendance("Kabir", creds)
add_attendance("Kabir", creds)
add_attendance("Sanchit", creds)
add_attendance("Shivang", creds)