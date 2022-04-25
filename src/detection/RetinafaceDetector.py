# # from retinaface import RetinaFace
# from face_detection import RetinaFace

# class RetinafaceDetector:
#     def __init__(self):
#         self.detector = RetinaFace(gpu_id=0)

#     def detect(self, frame):
#         faces = self.detector(frame)
        
#         bboxes = [tuple((
#             face[0][0],
#             face[0][1],
#             face[0][2] - face[0][0],
#             face[0][3] - face[0][1]
#             )
#         ) for face in faces if face[2] >= 0.9]
#         return bboxes

class RetinafaceDetector:
    def __init__(self):
        pass
    
    def detect(self, frame):
        pass