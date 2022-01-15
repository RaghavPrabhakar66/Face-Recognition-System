# from fdet import io, RetinaFace

# class RetinafaceDetector:
#     def __init__(self, backbone='RESNET50'):           # RESNET50(accurate) or MOBILENET(fast)
#         self.detector = RetinaFace(backbone=backbone)

#     def detect(self, frame):

#         dets = self.detector.detect(frame)
#         bboxes = [tuple(d['box']) for d in dets]
#         # landmarks = [d['keypoints'] for d in dets]

#         return bboxes, []

# '''FORMAT: list of dicts
#     [
#         {
#             'box': [511, 47, 35, 45],
#             'confidence': 0.9999996423721313,
#             'keypoints': {
#                 'left_eye': [517, 70],
#                 'right_eye': [530, 65],
#                 'nose': [520, 77],
#                 'mouth_left': [522, 87],
#                 'mouth_right': [531, 83]
#             }
#         }
#         .
#         .
#         .
#     ]
# '''