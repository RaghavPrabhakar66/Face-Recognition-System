# from arcface import ArcFace
# import numpy as np

# face_recognition = ArcFace.ArcFace()

# class ArcFaceRecognizer():
#     def __init__(self, database):
#         self.embed = face_recognition._calc_emb
#         self.compare = face_recognition.compare_faces
#         self.dist = face_recognition.get_distance_embeddings
#         self.database_embeddings = [self.embed(image)[0] for (_, image) in database]
#         self.database = database

#     def recognize(self, face):
#         face_embeddings = self.embed(face)
#         if not face_embeddings:
#             return None, None
#         matches = self.compare(self.database_embeddings, face_embeddings[0])
#         dists = face_recognition.face_distance(self.database_embeddings, face_embeddings[0])
#         index = np.argmin(dists)

#         if matches[index]:
#             return self.database[index]
#         else:
#             return None, None