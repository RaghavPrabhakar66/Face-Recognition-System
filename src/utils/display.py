import threading
import time
import os
from datetime import datetime
import cv2
import dlib
import numpy as np
from motpy import Detection, MultiObjectTracker

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
from src.utils.utilities import facial_extraction, load_database, record


def stream(
    filepath=None,
    # resize_shape=None,
    # scale=None,
    model="RetinaFace",
    extract_face=False,
    align_face=False,
    track_face=False,
    recognize_face=False,
    padding=0,
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

    known_tracks = {}

    # Frame rate
    dt = 1 / 15
    prev_frame_time = 0
    fps = 0
    frameCounter = 0
    step = 4

    # Load database
    database = load_database(path['database'])

    # Models
    detector = detector_wrapper(model)
    if recognize_face:
        recognizer = recognizer_wrapper('face_recognition', database)
    if track_face:
        tracker = MultiObjectTracker(dt=dt, model_spec=model_spec)

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

        # Calculate frame rate
        height, width, _ = frame.shape
        curr_frame_time = time.time()
        fps += round(1 / (curr_frame_time - prev_frame_time))
        prev_frame_time = curr_frame_time

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
            # lol = datetime.now()
            bboxes = detector.detect(frame)
            # print((datetime.now() - lol))
            for bbox in bboxes:
                detections.append(
                    Detection(
                        box=np.array(
                            [
                                bbox[0],
                                bbox[1],
                                bbox[0] + bbox[2],
                                bbox[1] + bbox[3],
                            ]
                        )
                    )
                )

        faces = []
        if track_face:
            tracker.step(detections)
            tracks = tracker.active_tracks(min_steps_alive=3)
        else:
            tracks = detections
        faces = []

        # Extract, align, recognize individual faces
        # And draw bounding boxes
        # if track_face:
        for track in tracks:
            track_color = [ord(c) * ord(c) % 256 for c in track.id[:3]] if track.id is not None else [255, 255, 255]
            face, (w, h)= facial_extraction(frame, track.box, padding=padding)
            if extract_face:
                # if align_face:
                #     face = align(frame, landmarks[i], w, h)
                faces.append(face)

            if recognize_face:
                if known_tracks.get(track.id, None) is None:
                    name, _ = recognizer.recognize(face)
                    known_tracks[track.id] = name
                    
                    if name:
                        os.makedirs(path['records'], exist_ok=True)
                        cv2.imwrite(path['records'] + '/' + str(known_tracks[track.id]) + '.jpg', face)
                        # cv2.rectangle(display_frame, (int(track.box[0]), int(track.box[1])), (int(track.box[0] + w), int(track.box[1] - 10)), track_color, -1)
                        cv2.putText(display_frame, known_tracks[track.id], (int(track.box[0] + 6), int(track.box[1] - 5)), FONT, FSCALE, [255, 255, 255], LTYPE)
                        record(name)
                    else:
                        # known_tracks[track.id] = 'unknown-' + str(track.id)
                        os.makedirs(path['records'], exist_ok=True)
                        cv2.imwrite(path['records'] + '/unknown-' + str(track.id) + '.jpg', face)
                        cv2.putText(display_frame, 'unknown', (int(track.box[0] + 6), int(track.box[1] - 5)), FONT, FSCALE, [255, 255, 255], LTYPE)
                else:
                    cv2.imwrite(path['records'] + '/' + str(known_tracks[track.id]) + '.jpg', face)
                    # cv2.rectangle(display_frame, (int(track.box[0]), int(track.box[1])), (int(track.box[0] + w), int(track.box[1] - 10)), track_color, -1)
                    cv2.putText(display_frame, known_tracks[track.id], (int(track.box[0] + 6), int(track.box[1] - 5)), FONT, FSCALE, [255, 255, 255], LTYPE)
                    
            display_frame = draw_bounding_box(
                display_frame,
                track.box,
                track_color,
                int(2 * scale),
                track.id,
            )
        
        # else:
        #     for i, det in enumerate(detections):
        #         face, (w, h)= facial_extraction(frame, det.box, padding=padding)

        #         if extract_face:
        #             cv2.imwrite(path['records'] + '/' + str(i) + '.png', face)
        #             # if align_face:
        #             #     face = align(frame, landmarks[i], w, h)
        #             faces.append(face)
                
        #         if recognize_face:
        #             name, _ = recognizer.recognize(face)
        #             if name:
        #                 cv2.putText(display_frame, name, (det.box[0] + 6, det.box[1] - 5), FONT, FSCALE, FONT_COLOR, LTYPE)

        #         display_frame = draw_bounding_box(
        #             display_frame,
        #             det.box,
        #             (0, 255, 0),
        #             2,
        #         )

        resultImage = cv2.hconcat(faces) if faces else display_frame

        # Display frame rate
        display_frame = cv2.resize(display_frame, resize_shape)
        cv2.putText(
            display_frame,
            f"FPS: {str(fps//frameCounter)}",
            (resize_shape[0] - 90, 30),
            FONT,
            FONT_SCALE,
            FONT_COLOR,
            LINETYPE,
        )

        # Display video and extracted faces
        cv2.imshow("base-image", display_frame)
        if extract_face:
            cv2.imshow("result-image", resultImage)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

