import face_recognition
import numpy as np

class Recognizer():
    def __init__(self):
        self.embed = face_recognition.face_encodings
        self.compare = face_recognition.compare_faces
        self.dist = face_recognition.face_distance
        self.database = np.load("D:\Python\Projects\Face-Recognition-System\data\embeddings\\names.npy", allow_pickle=True)
        self.database_embeddings = np.load("D:\Python\Projects\Face-Recognition-System\data\embeddings\embeddings.npy", allow_pickle=True)
        # for name, image in self.database:
        #     emb = self.embed(image)
        #     if len(emb) != 0:
        #         self.database_embeddings.append(emb[0])
        #         print(name, 'loaded')
        #     else:
        #         print(name, 'not loaded')

    def recognize(self, face):
        face_embeddings = self.embed(face)
        if not face_embeddings:
            return None
        matches = self.compare(self.database_embeddings, face_embeddings[0])
        dists = face_recognition.face_distance(self.database_embeddings, face_embeddings[0])
        index = np.argmin(dists)

        if matches[index]:
            res = self.database[index]
        else:
            res = None

        print(res)
        return res
