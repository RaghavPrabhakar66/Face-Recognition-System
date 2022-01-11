import time

import cv2

from src.detection.detector import Detectors

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.5
FONT_COLOR = (255, 0, 0)
LINETYPE = 2


def display_video(
    filepath=None,
    resize_shape=None,
    scale=None,
    model="Mediapipe",
    extract_face=False,
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

        if curr_frame_id % 5 == 0:
            results = detector.detect(frame)

        grid = []
        for bbox in results:
            x, y, w, h = bbox
            if extract_face:
                face = cv2.resize(
                    frame[y - 50 : y + h + 50, x - 50 : x + w + 50], (256, 256)
                )
                grid.append(face)
            else:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
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
            cv2.imshow("faces", faces)
        else:
            cv2.imshow("frame", frame)
        curr_frame_id += 1

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    print(f"Average FPS: {a//curr_frame_id}")
    cap.release()
    cv2.destroyAllWindows()
