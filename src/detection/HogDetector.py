import dlib


class HogDetector:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()

    def detect(self, frame):
        bboxes = []
        # landmarks = []
        dets = self.detector(frame, 1)
        for k, d in enumerate(dets):
            bboxes.append(
                (d.left(), d.top(), d.right() - d.left(), d.bottom() - d.top())
            )
            # shape = self.predictor(frame, d)
            # landmarks.append([(p.x, p.y) for p in shape.parts()])
        return bboxes
