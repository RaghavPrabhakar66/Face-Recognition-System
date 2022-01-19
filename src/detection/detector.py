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
# from RetinafaceDetector import RetinafaceDetector


models = {
    "HaarCascade": HaarCascadeDetector,
    "Mediapipe": MediapipeFaceDetector.A,
    "HOG": HogDetector,
    "MMOD": HogDetector,
    "MTCNN": MTCNNDetector,
    # 'RetinaNet': RetinafaceDetector,
}


class Detection:
    def __init__(
        self,
        box: np.ndarray,
        score: Optional[float] = None,
        class_id: Optional[int] = None,
        feature: Optional[np.ndarray] = None,
    ):
        self.box = box
        self.score = score
        self.class_id = class_id
        self.feature = feature


def detector_wrapper(model: str):
    a = models[model]
    return a()
