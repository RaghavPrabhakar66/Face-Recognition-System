import mediapipe as mp


class FaceDetector:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils

    def detect(self, frame):
        return self.face_detection.process(frame)
