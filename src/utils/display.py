import threading
import time

import cv2
import dlib
import numpy as np
from motpy import Detection, MultiObjectTracker

from src.detection.detector import Detection, detector_wrapper
from src.utils.draw import (
    FONT,
    FONT_COLOR,
    FONT_SCALE,
    LINETYPE,
    draw_bounding_box,
)


def extract(image, bbox, padding, size=(256, 256)):
    x, y, _, _ = bbox
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x, y, w, h = round(x), round(y), round(w), round(h)

    start_y, end_y = y - padding, y + h + padding
    start_x, end_x = x - padding, x + w + padding
    if start_y < 0:
        start_y = 0
    if end_y > image.shape[0]:
        end_y = image.shape[0]
    if start_x < 0:
        start_x = 0
    if end_x > image.shape[1]:
        end_x = image.shape[1]

    ratio = image.shape[1] // image.shape[0]
    try:
        face = cv2.resize(image[start_y:end_y, start_x:end_x], (size[0], ratio * size[0]))
    except:
        face = cv2.resize(image, (size[0], ratio * size[0]))

    return face


def doRecognizePerson(faceNames, fid):
    faceNames[fid] = "Person " + str(fid)


def display_video_motpy(
    filepath=None,
    resize_shape=None,
    scale=None,
    model="Mediapipe",
    extract_face=False,
    align_face=False,
    track_face=False,
    padding=20,
):
    detector = detector_wrapper(model)

    model_spec = {
        "order_pos": 1,
        "dim_pos": 2,
        "order_size": 0,
        "dim_size": 2,
        "q_var_pos": 5000.0,
        "r_var_pos": 0.1,
    }

    dt = 1 / 15  # assume 15 fps
    if track_face:
        tracker = MultiObjectTracker(dt=dt, model_spec=model_spec)

    # Video and webcam capture modes
    cap = (
        cv2.VideoCapture(0) if filepath is None else cv2.VideoCapture(filepath)
    )

    prev_frame_time = 0
    fps = 0
    frameCounter = 0
        
    # Create and position two opencv named windows
    cv2.namedWindow("base-image", cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow("base-image", 100, 100)
    if extract_face:
        cv2.namedWindow("result-image", cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow("result-image", 900, 100)        

    # Start the window thread for the two windows we are using
    if extract_face:
        cv2.startWindowThread()
        
    temp = np.zeros((1000, 1000, 3))
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break
        
        # Calculate frame rate
        height, width, _ = frame.shape
        curr_frame_time = time.time()
        fps += round(1 / (curr_frame_time - prev_frame_time))
        prev_frame_time = curr_frame_time

        # Reshape frame
        if resize_shape is not None:
            frame = cv2.resize(frame, resize_shape)
        elif scale is not None:
            frame = cv2.resize(
                frame, (int(width * scale), int(height * scale))
            )
        

        temp = cv2.resize(temp, (width, height))
        frameCounter += 1
        step = 1
        
        if not track_face:
            step = 1
        detections = []
        if frameCounter % step == 0:
            bboxes, _ = detector.detect(frame)

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
                        ),
                        score=None,
                        class_id=None,
                        feature=None,
                    )
                )

        if track_face:
            tracker.step(detections)
            tracks = tracker.active_tracks(min_steps_alive=3)

        faces = []
        if track_face:
            for track in tracks:
                # Extract individual faces
                if extract_face:
                    faces.append(extract(frame, track.box, padding=padding))
                print(track)

                frame = draw_bounding_box(
                    frame,
                    track.box,
                    [ord(c) * ord(c) % 256 for c in track.id[:3]],
                    2,
                    temp,
                )
                # pos = (track.box[0], track.box[3]) if text_at_bottom else (track.box[0], track.box[1])
                # text = track_to_string(track) if text_verbose == 2 else track.id[:8]
                # draw_text(frame, text, pos=pos)
        else:
            for det in detections:
                # Extract individual faces
                if extract_face:
                    faces.append(extract(frame, det.box, padding=padding))

                frame = draw_bounding_box(
                    frame,
                    det.box,
                    (0, 255, 0),
                    2,
                    temp,
                )

        resultImage = cv2.hconcat(faces) if faces else frame

        # Display frame rate
        cv2.putText(
            frame,
            f"FPS: {str(fps//frameCounter)}",
            (width - 90, 30),
            FONT,
            FONT_SCALE,
            FONT_COLOR,
            LINETYPE,
        )
        
        # Display video and extracted faces
        cv2.imshow("base-image", frame)
        cv2.imshow("result-image", resultImage)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def display_video(
    filepath=None,
    resize_shape=None,
    scale=None,
    model="Mediapipe",
    extract_face=False,
    align_face=False,
):
    detector = detector_wrapper(model)
    cap = (
        cv2.VideoCapture(0) if filepath is None else cv2.VideoCapture(filepath)
    )
    prev_frame_time = curr_frame_time = a = 0
    
    padding = 20

    # Create two opencv named windows
    cv2.namedWindow("base-image", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("result-image", cv2.WINDOW_AUTOSIZE)

    # Position the windows next to eachother
    cv2.moveWindow("base-image", 100, 100)
    cv2.moveWindow("result-image", 900, 100)

    # Start the window thread for the two windows we are using
    cv2.startWindowThread()

    # variables holding the current frame number and the current faceid
    frameCounter = 0
    currentFaceID = 0

    # Variables holding the correlation trackers and the name per faceid
    faceTrackers = {}
    faceNames = {}

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

        frameCounter += 1

        # Update all the trackers and remove the ones for which the update
        # indicated the quality was not good enough
        fidsToDelete = []
        for fid in faceTrackers.keys():
            trackingQuality = faceTrackers[fid].update(frame)

            # If the tracking quality is good enough, we must delete
            # this tracker
            if trackingQuality < 5:
                fidsToDelete.append(fid)

        for fid in fidsToDelete:
            print("Removing tracker " + str(fid) + " from list of trackers")
            faceTrackers.pop(fid, None)

        if frameCounter % 5 == 0:
            bboxes, landmarks = detector.detect(frame)

            for (_x, _y, _w, _h) in bboxes:
                x = int(_x)
                y = int(_y)
                w = int(_w)
                h = int(_h)

                # calculate the centerpoint
                x_bar = x + 0.5 * w
                y_bar = y + 0.5 * h

                # Variable holding information which faceid we
                # matched with
                matchedFid = None

                # Now loop over all the trackers and check if the
                # centerpoint of the face is within the box of a
                # tracker

                for fid in faceTrackers.keys():
                    tracked_position = faceTrackers[fid].get_position()

                    t_x = int(tracked_position.left())
                    t_y = int(tracked_position.top())
                    t_w = int(tracked_position.width())
                    t_h = int(tracked_position.height())

                    # calculate the centerpoint
                    t_x_bar = t_x + 0.5 * t_w
                    t_y_bar = t_y + 0.5 * t_h

                    # check if the centerpoint of the face is within the
                    # rectangleof a tracker region. Also, the centerpoint
                    # of the tracker region must be within the region
                    # detected as a face. If both of these conditions hold
                    # we have a match

                    if (
                        (t_x <= x_bar <= (t_x + t_w))
                        and (t_y <= y_bar <= (t_y + t_h))
                        and (x <= t_x_bar <= (x + w))
                        and (y <= t_y_bar <= (y + h))
                    ):
                        matchedFid = fid

                # If no matched fid, then we have to create a new tracker
                if matchedFid is None:
                    print("Creating new tracker " + str(currentFaceID))

                    # Create and store the tracker
                    tracker = dlib.correlation_tracker()
                    tracker.start_track(
                        frame,
                        dlib.rectangle(x - 10, y - 20, x + w + 10, y + h + 20),
                    )

                    faceTrackers[currentFaceID] = tracker

                    # Start a new thread that is going to be used to
                    # recoginze the face
                    t = threading.Thread(
                        target=doRecognizePerson,
                        args=(faceNames, currentFaceID),
                    )
                    t.start()

                    # Increase the currentFaceID counter
                    currentFaceID += 1

        # Now loop over all the trackers we have and draw the rectangle
        # around the detected faces. If we 'know' the name for this person
        # (i.e. the recognition thread is finished), we print the name
        # of the person, otherwise the message indicating we are detecting
        # the name of the person
        faces = []
        face = frame.copy()
        for fid in faceTrackers.keys():
            tracked_position = faceTrackers[fid].get_position()

            t_x = int(tracked_position.left())
            t_y = int(tracked_position.top())
            t_w = int(tracked_position.width())
            t_h = int(tracked_position.height())

            if fid in faceNames.keys():
                face = extract(frame, [t_x, t_y, t_w, t_h], padding=padding)
                faces.append(face)
                cv2.putText(
                    frame,
                    faceNames[fid],
                    (int(t_x + t_w / 2), int(t_y)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255),
                    2,
                )
            else:
                cv2.putText(
                    frame,
                    "Detecting...",
                    (int(t_x + t_w / 2), int(t_y)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255),
                    2,
                )

            cv2.rectangle(
                frame, (t_x, t_y), (t_x + t_w, t_y + t_h), (0, 255, 0), 2
            )

        resultImage = cv2.hconcat(faces) if faces else frame
        cv2.putText(
            frame,
            f"FPS: {str(a//frameCounter)}",
            (width - 90, 30),
            FONT,
            FONT_SCALE,
            FONT_COLOR,
            LINETYPE,
        )

        cv2.imshow("base-image", frame)
        cv2.imshow("result-image", resultImage)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
