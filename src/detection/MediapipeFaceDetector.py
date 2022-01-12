import cv2
import mediapipe as mp


class A:
    def __init__(self):
        print("Initializing mediapipe face detector")
        self.face_detection = mp.solutions.face_detection.FaceDetection(
            model_selection=1, min_detection_confidence=0.5
        )
        self.get_key_point = mp.solutions.face_detection.get_key_point
        self.keys = mp.solutions.face_detection.FaceKeyPoint

    def detect(self, image):
        results = self.face_detection.process(
            cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        )

        if results.detections is None:
            return [], []

        bboxes = []
        landmarks = []
        height, width, _ = image.shape
        for detection in results.detections:
            bboxes.append(
                [
                    round(
                        detection.location_data.relative_bounding_box.xmin
                        * width
                    ),
                    round(
                        detection.location_data.relative_bounding_box.ymin
                        * height
                    ),
                    round(
                        detection.location_data.relative_bounding_box.width
                        * width
                    ),
                    round(
                        detection.location_data.relative_bounding_box.height
                        * height
                    ),
                ]
            )
            landmarks.append(
                {
                    "LEFT_EYE": [
                        round(
                            detection.location_data.relative_keypoints[1].x
                            * width
                        ),
                        round(
                            detection.location_data.relative_keypoints[1].y
                            * height
                        ),
                    ],
                    "RIGHT_EYE": [
                        round(
                            detection.location_data.relative_keypoints[0].x
                            * width
                        ),
                        round(
                            detection.location_data.relative_keypoints[0].x
                            * height
                        ),
                    ],
                }
            )

        return bboxes, landmarks
