import cv2
import time
import numpy as np
from expression_api.Emotion_detection import EmotionDetect
from expression_api.utils import *
from expression_api.Face_detection import DetectFace

params = get_face_model()
FaceDetector = DetectFace(params)

EmotionDetector = EmotionDetect(emotion_model)


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # print(image.shape)

        ret, jpeg = cv2.imencode('.jpg', image)
        Image = cv2.resize(image, (48, 48))
        faces = FaceDetector.get_faces_from_frame(image)

        emotion_arr = []
        for face in faces:
            (startX, startY, endX, endY, confidence) = face
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            roi_gray = gray[startY:endY, startX:endX]
            cropped_img = convert_gray2rgb(cv2.resize(roi_gray, (48, 48)))
            emotion, e_confidence, prediction = EmotionDetector.PredictEmotion(
                cropped_img)
            emotion_arr = [emotion, e_confidence]
            # print(emotion)

        return image, emotion_arr, jpeg.tobytes()


def gen(camera):
    emotion_logs = []
    emotion_dict = {}
    for i in range(0, 3):
        image, emotion_arr, frame = camera.get_frame()
        try:
            emotion_logs.append(emotion_arr)
            emotion_dict[str(i)] = emotion_arr
        except:
            pass
        image = cv2.resize(image, (48, 48))
        # print(image.shape)
        # print(frame)
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        # time.sleep(5)

    emotion_logs = np.array(emotion_logs)
    np.savetxt('./expression_api/emotion_logs.txt', emotion_logs, fmt='%s')
    print('emotion_dict',emotion_dict)



def convert_gray2rgb(image):
    width, height = image.shape
    out = np.empty((width, height, 3), dtype=np.uint8)
    out[:, :, 0] = image
    out[:, :, 1] = image
    out[:, :, 2] = image
    print(out.shape)
    out = out.reshape(1, 48, 48, 3)
    return out
