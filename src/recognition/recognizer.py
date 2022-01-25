import face_recognition
import numpy as np

class Recognizer():
    def __init__(self, database):
        self.embed = face_recognition.face_encodings
        self.compare = face_recognition.compare_faces
        self.dist = face_recognition.face_distance
        self.database_embeddings = [self.embed(image)[0] for (_, image) in database]
        self.database = database

    def recognize(self, face):
        face_embeddings = self.embed(face)
        if not face_embeddings:
            return None, None
        matches = self.compare(self.database_embeddings, face_embeddings[0])
        dists = face_recognition.face_distance(self.database_embeddings, face_embeddings[0])
        index = np.argmin(dists)

        if matches[index]:
            return self.database[index]
        else:
            return None, None

# class X-recognizer():
#     def __init__(self, database): # (imgName, img)
#         self.database = embed(database)
    
#     def recognize(self, img):
#         name = compare(img, self.database)

#         return name   