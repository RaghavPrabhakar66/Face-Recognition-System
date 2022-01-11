"""
detector = Detector('Haar Cascade') # intialize detector

for img in imgs:
    detector.detect(img) # detect faces in image
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


import MediapipeFaceDetector
from HaarCascadeDetector import HaarCascadeDetector
from MTCNNDetector import MTCNNDetector


class Detectors:
    def __init__(self):
        self.models = {
            "Haar Cascade": HaarCascadeDetector(),
            "Mediapipe": MediapipeFaceDetector.A(),
            "MTCNN": MTCNNDetector(),
        }

    def loadModel(self, model: str):
        return self.models[model]
