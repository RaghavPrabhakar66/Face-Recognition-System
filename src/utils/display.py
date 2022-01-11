import time

import cv2

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
        for bbox in results:
            x, y, w, h = bbox
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face = cv2.resize(frame[y:y+h, x:x+w], (256, 256))
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
