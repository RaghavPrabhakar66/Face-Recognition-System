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
from HogDetector import HogDetector
from MTCNNDetector import MTCNNDetector

models = {
    "Haar Cascade": HaarCascadeDetector,
    "Mediapipe": MediapipeFaceDetector.A,
    "HOG": HogDetector,
    "MMOD": HogDetector,
    "MTCNN": MTCNNDetector,
}


def detector_wrapper(model: str):
    a = models[model]
    return a()
