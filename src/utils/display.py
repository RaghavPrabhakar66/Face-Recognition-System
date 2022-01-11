import time

import cv2
import numpy as np

from src.detection.detector import Detectors
import matplotlib.pyplot as plt

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.5
FONT_COLOR = (255, 0, 0)
LINETYPE = 2


def display_video(filepath=None, resize_shape=None, scale=None, model='Mediapipe'):
    detector = Detectors().loadModel(model)
    if filepath is None:
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(filepath)
    prev_frame_time = curr_frame_time = curr_frame_id = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        height, width, _ = frame.shape
        curr_frame_time = time.time()
        fps = int(1 / (curr_frame_time - prev_frame_time))
        prev_frame_time = curr_frame_time

        if resize_shape is not None:
            frame = cv2.resize(frame, resize_shape)
        elif scale is not None:
            frame = cv2.resize(frame, (int(width * scale), int(height * scale)))

        if curr_frame_id % 1 == 0:
            results = detector.detect(frame)
        
        grid = []
        angle = 0
        face = frame
        padding = 100
        for bbox, landmarks  in results:
            # Cropping
            x, y, w, h = bbox
            center = (w//2 + padding, h//2 + padding)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face = frame[y - padding: y + h + padding, x - padding: x + w + padding]
            face = cv2.resize(face, (256, 256))

            # Allignment - Rotation only no stretching
            l, r = landmarks['LEFT_EYE'], landmarks['RIGHT_EYE']
            angle = (np.arctan((r[1] - l[1])/(r[0] - l[0])) * 180) / np.pi
            rot = cv2.getRotationMatrix2D(center, (angle), 1.0)
            face = cv2.warpAffine(face, rot, (w, h))

            grid.append(face)
        faces = cv2.hconcat(grid)


        cv2.putText(
            frame,
            f"FPS: {str(fps)}",
            (width - 90, 30),
            FONT,
            FONT_SCALE,
            FONT_COLOR,
            LINETYPE,
        )
        if faces is not None:
            cv2.imshow("frame", faces)
        else:
            cv2.imshow("frame", frame)
        curr_frame_id += 1

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
