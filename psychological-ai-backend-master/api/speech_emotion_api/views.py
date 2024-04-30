from django.contrib.auth.models import User

# Create your views here.
from rest_framework import views
from rest_framework.response import Response

from flask import Flask, jsonify
import tensorflow as tf
import librosa
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

global model

file1 = open("E:\projects\psychological-ai-backend\\api\\speech_emotion_api\Ylist.txt", "r")
x = file1.read()
x = x.split(",")
Y = []
for i in range(len(x)):
    if (x[i] == "," or x[i] == " "):
        continue
    Y.append(x[i])
# print(len(Y))

encoder = OneHotEncoder()
Y = encoder.fit_transform(np.array(Y).reshape(-1, 1)).toarray()

model = tf.keras.models.load_model("E:\projects\psychological-ai-backend\\api\speech_emotion_api\Model")


def noise(data_point):
    amp = 0.035 * np.random.uniform() * np.amax(data_point)
    incr = amp * np.random.normal(size=data_point.shape[0])
    data_point = data_point + incr
    return data_point


def stretch(data_point):
    rate = 0.8
    return librosa.effects.time_stretch(data_point, rate)


def shift(data_point):
    shift_range = int(np.random.uniform(low=-5, high=5) * 1000)
    return np.roll(data_point, shift_range)


def pitch(data_point, sampling_rate):
    pitch_factor = 0.7
    return librosa.effects.pitch_shift(data_point, sampling_rate, pitch_factor)


def extract_features(data_point, sampling_rate):
    result = np.array([])
    # 1. Zero Crossing Rate
    # .T is the transpose
    zcr = np.mean(librosa.feature.zero_crossing_rate(y=data_point).T, axis=0)
    # to stack horizontally, use hstack()
    result = np.hstack((result, zcr))

    # 2. Chroma_stft
    stft = np.abs(librosa.stft(data_point))
    chroma_stft = np.mean(librosa.feature.chroma_stft
                          (S=stft, sr=sampling_rate).T, axis=0)
    # stack horizontally
    result = np.hstack((result, chroma_stft))

    # 3. MFCC(Mel Frequency Cepstral Coefficients)
    mfcc = np.mean(librosa.feature.mfcc
                   (y=data_point, sr=sampling_rate).T, axis=0)
    # stack horizontally
    result = np.hstack((result, mfcc))

    # 4. Root Mean Square
    rms = np.mean(librosa.feature.rms
                  (y=data_point).T, axis=0)
    # stack horizontally
    result = np.hstack((result, rms))

    # 5. Mel Spectrogram
    mel = np.mean(librosa.feature.melspectrogram
                  (y=data_point, sr=sampling_rate).T, axis=0)
    # stack horizontally
    result = np.hstack((result, mel))

    # 6. Spectral rolloff
    rolloff = np.mean(librosa.feature.spectral_rolloff
                      (y=data_point, sr=sampling_rate).T, axis=0)
    # stack horizontally
    result = np.hstack((result, rolloff))

    # 7. Spectral centroid
    centroid = np.mean(librosa.feature.spectral_centroid
                       (y=data_point, sr=sampling_rate).T, axis=0)
    # stack horizontally
    result = np.hstack((result, centroid))
    return result


def get_features(path):
    # duration and offset : for the empty audio in start and end of each file
    data_point, sampling_rate = librosa.load(path, duration=2.5, offset=0.6)

    # extract features of normal audio
    temp1 = extract_features(data_point, sampling_rate)
    result = np.array(temp1)

    # extract features of noisy audio
    # first get noisy data using noise(data)
    # then extract features
    noisy_data = noise(data_point)
    temp2 = extract_features(noisy_data, sampling_rate)
    # use vstack to stack vertically
    result = np.vstack((result, temp2))

    # extract features of stretched and pitched audio
    # first get stretched data using stretch(data)
    # next send this stretched data as parameter to get pitched stretched data
    # then extract features
    stretched_data = stretch(data_point)
    pitched_stretched_data = pitch(stretched_data, sampling_rate)
    temp3 = extract_features(pitched_stretched_data, sampling_rate)
    result = np.vstack((result, temp3))

    return result


def PredictEmotion(f):
    prediction = model.predict(f)
    y_pred = encoder.inverse_transform(prediction)

    max_index = int(np.argmax(prediction))
    if (0 <= max_index <= 7):
        ind = 0
    if (8 <= max_index <= 15):
        ind = 1
    if (16 <= max_index <= 23):
        ind = 2
    return [y_pred[ind], np.max(prediction)]


# def testing(newfile):
#     feature = get_features(newfile)
#     # print(feature)
#
#     # make features dataframe
#     Features = pd.DataFrame(feature)
#     Features.to_csv('features.csv', index=False)
#     # Features.head()
#
#     scaler = StandardScaler()
#     feature = scaler.fit_transform(feature)
#     feature = np.expand_dims(feature, axis=2)
#     # print(f'Features extracted: {feature.shape[1]}')
#
#     test_point = model.predict(feature)
#     y_pred = encoder.inverse_transform(test_point)
#
#     new = []
#     for i in range(len(y_pred)):
#         for j in range(len(y_pred[i])):
#             new.append(y_pred[i][j])
#     # print(new)
#
#     max = 0
#     res = new[0]
#     for i in new:
#         freq = new.count(i)
#         if freq > max:
#             max = freq
#             res = i
#     new = []
#     for i in range(len(y_pred)):
#         for j in range(len(y_pred[i])):
#             new.append(y_pred[i][j])
#
#     max = 0
#     res = new[0]
#     for i in new:
#         freq = new.count(i)
#         if freq > max:
#             max = freq
#             res = i
#
#     # print ("Emotion detected is : " + str(res))
#     return new, max*1.0/3

def testing(newfile):
    feature = get_features(newfile)
    # print(feature)

    # make features dataframe
    Features = pd.DataFrame(feature)
    Features.to_csv('features.csv', index=False)
    # Features.head()
    print("Features:", Features)

    scaler = StandardScaler()
    feature = scaler.fit_transform(feature)
    feature = np.expand_dims(feature, axis=2)

    y_pred = []
    y_pred.append(PredictEmotion(feature))
    print(y_pred[0][0][0], y_pred[0][1],'yyyyyyyyyyyyyyyy')
    return [y_pred[0][0][0]], y_pred[0][1]


class SpeechEmotionView(views.APIView):

    def get(self, request):
        # filepath = "E:\\Study\\7th sem\\Project\\Tess\\TESS Toronto emotional speech set data\\OAF_disgust\\OAF_back_disgust.wav"
        emotion, per = testing(
            "E:\projects\psychological-ai-backend\\api\\voice_to_voice\\recording\classify\Activity_or_situation_that_reminds_you_of_a_particular_event,_does_that_trigger_a_very_large_and_adverse_response_in_you.wav")
        return Response({"Emotion": emotion, "Severity": per})
