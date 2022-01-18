import cv2
import numpy as np

def align(face, landmarks, width, height, ideal_left_eye=(0.35, 0.35)):
    '''Aligns a list of face images according to given landmarks'''
    (lx, ly), (rx, ry) = landmarks['LEFT_EYE'], landmarks['RIGHT_EYE']

    # Angle
    dy, dx = ry - ly, rx - lx
    angle = np.degrees(np.arctan2(dy, dx)) + 180
    print(angle)
    # Scale
    dist = np.sqrt((dy ** 2) + (dx ** 2))
    desiredDist = (1 - 2 * ideal_left_eye[0]) * width
    scale = desiredDist / dist

    # Center
    center = ((lx + rx) // 2, (ly + ry) // 2)

    # Rotate image
    rot = cv2.getRotationMatrix2D(center, angle, scale)

    # Translate image so that face is still in view
    tX = width * 0.5
    tY = height * ideal_left_eye[1]
    rot[0, 2] += (tX - center[0])
    rot[1, 2] += (tY - center[1])

    face = cv2.warpAffine(face, rot, (width, height), flags=cv2.INTER_CUBIC)

    return face
