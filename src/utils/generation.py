import cv2
import numpy as np
from face_recognition import face_encodings
from src.detection.detector import detector_wrapper
import requests
from tqdm import tqdm
from sklearn import svm
from pickle import dump

# get different angles, store array
def generate(embedding_model=face_encodings, detection_model='RetinaFace', frame_count=2, skip=24):
    embedding_map = []
    name_map = []
    videos = get_videos()
    detection_model = detector_wrapper(detection_model)
    face_classifier = svm.SVC(gamma='scale')
    
    for name, video in tqdm(videos, total=len(videos)):
        embeddings = []
        names = []
        cap = cv2.VideoCapture(video)
        
        f = frame_count
        i = 0
        while f > 1:
            ret, frame = cap.read()
            if not ret:
                break
            bboxes = detection_model.detect(frame)

            if i % skip == 0 and bboxes is not None:
                emb = embedding_model(frame)
                if len(emb) != 0:
                    embeddings.append(emb[0])
                    names.append(name)
                    cv2.imwrite("D:\Python\Projects\Face-Recognition-System\data\embeddings\{}.png".format(name+'_'+str(i)), frame)
                f -= 1
            i += 1
        

        embedding_map.extend(embeddings)
        name_map.extend(names)
        cap.release()  
        cv2.destroyAllWindows()
    
    
    face_classifier.fit(embedding_map, name_map)
    
    with open('D:\Python\Projects\Face-Recognition-System\data\embeddings\svm.pkl', 'wb') as f:
        dump(face_classifier, f)

    # np.save("D:\Python\Projects\Face-Recognition-System\data\embeddings\embeddings.npy", embedding_map, allow_pickle=True)
    # np.save("D:\Python\Projects\Face-Recognition-System\data\embeddings\\names.npy", name_map, allow_pickle=True)


    print("Embeddings generated")
    return embedding_map, name_map


def get_videos():
    student_url = 'http://127.0.0.1:8080/api/students'
    students = requests.get(student_url, auth=('a@a.com', 'admin')).json()
    path = "D:/Python/Projects/Face-Recognition-System/data/database/"
    videos = [[student['first_name'], path + student['video'].split('/')[-1]] for student in students]
    return videos