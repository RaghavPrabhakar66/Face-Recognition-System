import time

import cv2
import numpy as np

from src.detection.detector import Detectors

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.5
FONT_COLOR = (255, 0, 0)
LINETYPE = 2


def align(face, l, r, width, height, padding):
    center = (width // 2 + padding, height // 2 + padding)
    angle = (np.arctan((r[1] - l[1]) / (r[0] - l[0])) * 180) / np.pi
    rot = cv2.getRotationMatrix2D(center, (angle), 1.0)
    face = cv2.warpAffine(face, rot, (width, height))

    return face


def extract(image, bbox, padding, size=(256, 256)):
    x, y, w, h = bbox
    start_y, end_y = y - padding, y + h + padding
    start_x, end_x = x - padding, x + w + padding
    if y - padding < 0:
        start_y = 0
    elif y + h + padding > image.shape[0]:
        end_y = image.shape[0]
    elif x - padding < 0:
        start_x = 0
    elif x + w + padding > image.shape[1]:
        end_x = image.shape[1]

    face = cv2.resize(image[start_y:end_y, start_x:end_x], size)

    return face


def display_video(
    filepath=None,
    resize_shape=None,
    scale=None,
    model="Mediapipe",
    extract_face=False,
    align_face=False,
):
    detector = Detectors().loadModel(model)
    cap = (
        cv2.VideoCapture(0) if filepath is None else cv2.VideoCapture(filepath)
    )
    prev_frame_time = curr_frame_time = curr_frame_id = a = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        height, width, _ = frame.shape
        curr_frame_time = time.time()
        fps = round(1 / (curr_frame_time - prev_frame_time))
        a += fps
        prev_frame_time = curr_frame_time

        if resize_shape is not None:
            frame = cv2.resize(frame, resize_shape)
        elif scale is not None:
            frame = cv2.resize(
                frame, (int(width * scale), int(height * scale))
            )

        if curr_frame_id % 2 == 0:
            bboxes, landmarks = detector.detect(frame)

        grid = []
        padding = 10
        for idx, bbox in enumerate(bboxes):
            # Cropping
            if extract_face:
                face = extract(frame, bbox, padding)

                if align_face:
                    # Allignment - Rotation only no stretching
                    face = align(
                        face,
                        landmarks[idx]["LEFT_EYE"],
                        landmarks[idx]["RIGHT_EYE"],
                        bbox[2],
                        bbox[3],
                        padding,
                        angle=0,
                    )

                grid.append(face)
            else:
                cv2.rectangle(
                    frame,
                    (bbox[0], bbox[1]),
                    (bbox[0] + bbox[2], bbox[1] + bbox[3]),
                    (0, 255, 0),
                    2,
                )

        frame = cv2.hconcat(grid) if grid else frame
        curr_frame_id += 1
        cv2.putText(
            frame,
            f"FPS: {str(a//curr_frame_id)}",
            (width - 90, 30),
            FONT,
            FONT_SCALE,
            FONT_COLOR,
            LINETYPE,
        )

        cv2.imshow("faces", frame)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    print(f"Average FPS: {a//curr_frame_id}")
    cap.release()
    cv2.destroyAllWindows()
