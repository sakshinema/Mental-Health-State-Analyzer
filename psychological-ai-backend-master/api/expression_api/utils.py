import cv2
import os
from django.conf import settings

BASE_DIR = settings.BASE_DIR

prototxt = os.path.join(BASE_DIR, 'Models/Face_detection/deploy.prototxt.txt')
face_model = os.path.join(BASE_DIR, 'Models/Face_detection/res10_300x300_ssd_iter_140000.caffemodel')
emotion_model = os.path.join(BASE_DIR, 'Models/Emotion_detection/model (9).h5')

COLOR_BLUE = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (0, 0, 255)
FONT = cv2.FONT_HERSHEY_SIMPLEX
THICKNESS = 2

def get_face_model():
    params = {
        'prototxt': prototxt,
        'model': face_model
    }
    return params