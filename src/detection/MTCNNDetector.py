import cv2


class MTCNNDetector:
    def load_model(self):
        from mtcnn import MTCNN

        self.detector = MTCNN()

    def detect(self, image):
        results = self.detector.detect_faces(
            cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        )

        if len(results) == 0:
            return []

        return [result["box"] for result in results]
