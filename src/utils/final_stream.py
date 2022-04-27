import threading
import time
import os
from datetime import datetime
import cv2
import numpy as np
from motpy import Detection, MultiObjectTracker
import uuid

from src.alignment.aligment import align
from src.recognition.recognition import recognizer_wrapper
from src.detection.detector import Detection, detector_wrapper
from src.utils.draw import (
    FONT,
    FONT_COLOR,
    FONT_SCALE,
    LINETYPE,
    draw_bounding_box,
)
from src.utils.utilities import facial_extraction, record, login


def stream2(
    filepath=None,
    # resize_shape=None,
    # scale=None,
    model="Mediapipe",
    extract_face=False,
    align_face=False,
    recognize_face=False,
    padding=0,
    status='entry'
):

    model_spec = {
        "order_pos": 1,
        "dim_pos": 2,
        "order_size": 0,
        "dim_size": 2,
        "q_var_pos": 5000.0,
        "r_var_pos": 0.1,
    }
    
    # Paths
    path = {
        'records': 'data/records/' + str(datetime.now().strftime('%d-%B-%Y')),
        'database': 'data/database',
    }

    # Frame rate
    dt = 1 / 20
    prev_frame_time = 0
    fps = 0
    frameCounter = 0
    step = 1

    # Login Backend
    creds = login(['a@a.com', 'admin'])
    print("Logged into backend")

    # Models
    detector = detector_wrapper(model)
    if recognize_face:
        recognizer = recognizer_wrapper('face_recognition')

    # Video and webcam capture modes
    cap = (
        cv2.VideoCapture(0) if filepath is None else cv2.VideoCapture(filepath)
    )

    # Create and position two opencv named windows
    cv2.namedWindow("base-image", cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow("base-image", 100, 100)

    if extract_face:
        cv2.namedWindow("result-image", cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow("result-image", 900, 100)

    # Start the window thread for the two windows we are using
    if extract_face:
        cv2.startWindowThread()
    
    resize_shape = None
    scale = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        display_frame = frame.copy()
        height, width, _ = frame.shape

        # # Calculate frame rate
        # curr_frame_time = time.time()
        # fps += round(1 / (curr_frame_time - prev_frame_time))
        # prev_frame_time = curr_frame_time

        # Reshape frame
        if resize_shape is None:
            resize_shape = (1000, int((height / width) * 1000))
        if scale is None:
            scale =  width / 800
            LTYPE = max(LINETYPE, int(scale * LINETYPE))
            FSCALE = max(FONT_SCALE, int(scale * FONT_SCALE))

        frameCounter += 1

        detections = []
        if frameCounter % step == 0:
            bboxes = detector.detect(frame)
            #print(bboxes)
            for bbox in bboxes:
                if len(bbox) == 4:
                    detections.append(
                        Detection(
                            box=np.array(
                                [
                                    bbox[0],
                                    bbox[1],
                                    bbox[0] + bbox[2],
                                    bbox[1] + bbox[3],
                                ]
                            ),
                            id=uuid.uuid1().hex
                        )
                    )

            faces = []

            for track in detections:
                track_color = [255, 255, 255]
                face, (w, h)= facial_extraction(frame, track.box, padding=padding)
                if extract_face:
                    # if align_face:
                    #     face = align(frame, landmarks[i], w, h)
                    faces.append(face)

                if recognize_face:
                    name = recognizer.recognize(face)
                    
                    if name:
                        os.makedirs(path['records'], exist_ok=True)
                        cv2.imwrite(path['records'] + '/' + name + '.jpg', face)
                        # cv2.rectangle(display_frame, (int(track.box[0]), int(track.box[1])), (int(track.box[0] + w), int(track.box[1] - 10)), track_color, -1)
                        cv2.putText(display_frame, name, (int(track.box[0] + 6), int(track.box[1] - 5)), FONT, FSCALE, [255, 255, 255], LTYPE)
                        record(name, creds, status)
                    else:
                        # known_tracks[track.id] = 'unknown-' + str(track.id)
                        os.makedirs(path['records'], exist_ok=True)
                        cv2.imwrite(path['records'] + '/unknown-' + str(track.id) + '.jpg', face)
                        cv2.putText(display_frame, 'unknown', (int(track.box[0] + 6), int(track.box[1] - 5)), FONT, FSCALE, [255, 255, 255], LTYPE)
                    
                        
                display_frame = draw_bounding_box(
                    display_frame,
                    track.box,
                    track_color,
                    int(2 * scale),
                    track.id,
                )

            resultImage = cv2.hconcat(faces) if faces else display_frame

            # # Display frame rate
            # display_frame = cv2.resize(display_frame, resize_shape)
            # cv2.putText(
            #     display_frame,
            #     f"FPS: {str(fps//frameCounter)}",
            #     (resize_shape[0] - 90, 30),
            #     FONT,
            #     FONT_SCALE,
            #     FONT_COLOR,
            #     LINETYPE,
            # )

            # Display video and extracted faces
            cv2.imshow("base-image", display_frame)
            if extract_face:
                cv2.imshow("result-image", resultImage)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()

