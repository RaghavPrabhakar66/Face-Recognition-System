from deepface import DeepFace

DeepFace.stream(
    db_path = "D:\Python\Projects\Face-Recognition-System\data\database",
    enable_face_analysis=False,
    model_name ='VGG-Face',
    detector_backend = 'ssd',
    time_threshold = 1,
    frame_threshold = 2)

# model_name : VGG-Face, Facenet, OpenFace, DeepFace, DeepID, Dlib or Ensemble
# detector_backend : opencv, ssd, mtcnn, dlib, retinaface