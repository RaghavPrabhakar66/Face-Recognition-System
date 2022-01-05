import os

import cv2

HAAR_CASCADES_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "./cascades/"
)


class HaarCascadeDetector:
    def __init__(self):
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
        return self.detectors["face"].detectMultiScale(
            image=image,
            scaleFactor=scaleFactor,
            minNeighbors=minNeighbors,
            minSize=minSize,
            flags=cv2.CASCADE_SCALE_IMAGE,
        )


if __name__ == "__main__":
    HaarCascadeDetector()
