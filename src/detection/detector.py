"""
detector = Detector('Haar Cascade') # intialize detector

for img in imgs:
    detector.detect(img) # detect faces in image
"""

import os
import sys
from typing import Optional

import numpy as np

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import MediapipeFaceDetector
from HaarCascadeDetector import HaarCascadeDetector
from HogDetector import HogDetector
from MTCNNDetector import MTCNNDetector
from RetinafaceDetector import RetinafaceDetector

# from RetinafaceDetector import RetinafaceDetector


models = {
    "HaarCascade": HaarCascadeDetector,
    "Mediapipe": MediapipeFaceDetector.A,
    "HOG": HogDetector,
    "MMOD": HogDetector,
    "MTCNN": MTCNNDetector,
    'RetinaFace': RetinafaceDetector,
}

class Detection:
    def __init__(
        self,
        box: np.ndarray,
        score: Optional[float] = None,
        class_id: Optional[int] = None,
        feature: Optional[np.ndarray] = None,
        id: str = None,
    ):
        self.box = box
        self.score = score
        self.class_id = class_id
        self.feature = feature
        self.id = id

    def set_id(self, idx):
        self.id = idx


def detector_wrapper(model: str):
    print(model)
    a = models[model]
    return a()
