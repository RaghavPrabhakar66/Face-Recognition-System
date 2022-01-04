import time

import cv2

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.5
FONT_COLOR = (255, 0, 0)
LINETYPE = 2


def display_video(filepath, resize_shape=None, scale=1.0):
    if filepath is None:
        cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(filepath)
    prev_frame_time = curr_frame_time = 0

    while cap.isOpened():
        ret, frame = cap.read()
        height, width, _ = frame.shape
        curr_frame_time = time.time()
        fps = int(1 / (curr_frame_time - prev_frame_time))
        prev_frame_time = curr_frame_time

        if not ret:
            break

        if resize_shape is not None:
            width, height = resize_shape
        elif scale is not None:
            width, height = int(width * scale), int(height * scale)

        frame = cv2.resize(frame, (width, height))

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

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
