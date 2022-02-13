import os

import cv2


class HaarCascadeDetector:
    def __init__(self):
        HAAR_CASCADES_PATH = os.path.join(
            os.path.dirname(os.path.realpath(cv2.__file__)), "data"
        )
        self.detectorPaths = {
            "face": "haarcascade_frontalface_default.xml",
            "eyes": "haarcascade_eye.xml",
            "smile": "haarcascade_smile.xml",
        }
        self.detectors = {}

        for (name, filename) in self.detectorPaths.items():
            self.detectors[name] = cv2.CascadeClassifier(
                os.path.join(HAAR_CASCADES_PATH, filename)
            )

    def detect(self, image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        face_bbox = self.detectors["face"].detectMultiScale(
            image=gray,
            scaleFactor=scaleFactor,
            minNeighbors=minNeighbors,
            minSize=minSize,
            flags=cv2.CASCADE_SCALE_IMAGE,
        )

        # eyes_bbox = []
        # for (x, y, w, h) in face_bbox:
        #     eyes = self.detectors["eyes"].detectMultiScale(
        #         gray[y : y + h, x : x + w]
        #     )
        #     if len(eyes) == 2:
        #         eyes_bbox.append({"LEFT_EYE": eyes[0], "RIGHT_EYE": eyes[1]})

        return face_bbox
