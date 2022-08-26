import face_recognition
import numpy as np
from pickle import load
import os

class Recognizer():
    def __init__(self):
        self.embed = face_recognition.face_encodings
        self.compare = face_recognition.compare_faces
        self.dist = face_recognition.face_distance
        # self.database = np.load("D:\Python\Projects\Face-Recognition-System\data\embeddings\\names.npy", allow_pickle=True)
        # self.database_embeddings = np.load("D:\Python\Projects\Face-Recognition-System\data\embeddings\embeddings.npy", allow_pickle=True)
        with open(os.path.abspath("data/embeddings/svm.pkl"), 'rb') as f:
            self.svm = load(f)
        print("Embeddings loaded")

        # self.annoy = AnnoyIndex(128, 'euclidean')
        # self.annoy.load()
        
    def recognize(self, face):
        face_embeddings = self.embed(face)
        if not face_embeddings:
            return None
        # matches = self.compare(self.database_embeddings, face_embeddings)
        # dists = face_recognition.face_distance(self.database_embeddings, face_embeddings)
        # index = np.argmin(dists)

        name = self.svm.predict(face_embeddings)
        proba = self.svm.predict_proba(face_embeddings)
        print(proba)
        return name[0]
        # if matches[index]:
        #     res = self.database[index]
        # else:
        #     res = None
        # return res
