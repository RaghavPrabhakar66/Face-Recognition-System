from recognizer import Recognizer

models = {
    'face_recognition': Recognizer,
}

def recognizer_wrapper(model: str, database):
    return models[model](database)

