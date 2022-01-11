import time

import cv2

from src.detection.detector import Detectors

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.5
FONT_COLOR = (255, 0, 0)
LINETYPE = 2

detector = Detectors().loadModel("Mediapipe")


def display_video(filepath, resize_shape=None, scale=1.0):
    if filepath is None:
        cap = cv2.VideoCapture(0)

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
            width, height = resize_shape
        elif scale is not None:
            width, height = int(width * scale), int(height * scale)

        frame = cv2.resize(frame, (width, height))
        results = detector.detect(frame)

        if curr_frame_id % 5 == 0:
            results = detector.detect(frame)

        for bbox in results:
            x, y, w, h = bbox
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(
            frame,
            f"FPS: {str(fps)}",
            (width - 90, 30),
            FONT,
            FONT_SCALE,
            FONT_COLOR,
            LINETYPE,
        )
        cv2.imshow("frame", frame)

        curr_frame_id += 1

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
