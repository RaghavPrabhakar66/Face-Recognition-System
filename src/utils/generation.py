import cv2
import os

# get different angles, store array
def generate(embedding_model, detection_model, frame_count=5):
    embedding_map = []
    videos = get_videos()
    for video in videos:
        embeddings = []
        cap = cv2.VideoCapture(video)
        f = frame_count
        while f > 1:
            _, frame = cap.read()
            bboxes, _ = detection_model(frame)
            face = frame[bboxes[0]:bboxes[2], bboxes[1]:bboxes[3]]
            embeddings.append(embedding_model(face))
            f -= 1
        embedding_map.append(embeddings)
        cap.release()  
        cv2.destroyAllWindows()  
    return embeddings


def get_videos():
    students = models.Students.objects.all()
    videos = [[student.id, student.video] for student in students]
    
    return videos