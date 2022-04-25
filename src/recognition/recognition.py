from src.recognition.recognizer import Recognizer

models = {
    'face_recognition': Recognizer,
}

def recognizer_wrapper(model: str):
    return models[model]()

