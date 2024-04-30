import numpy as np
import tensorflow as tf

class EmotionDetect:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self.get_model()

    def get_model(self):
        model = tf.keras.models.load_model('Models/Emotion_detection/model (9).h5')
        return model

    def PredictEmotion(self, Image):
        emotion_dict = {0:'angry', 1:'disgust', 2:'fear', 3:'happy', 4:'sad', 5:'surprise', 6:'neutral'}
        prediction = self.model.predict(Image)
        max_index = int(np.argmax(prediction))
        return emotion_dict[max_index], np.max(prediction), prediction