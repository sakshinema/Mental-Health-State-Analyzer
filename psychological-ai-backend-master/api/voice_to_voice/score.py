def score_calc(face_arr,speech_arr,quest_arr):
    emotion_score = []
    emotions = []
    for face_score,speech_score in zip(face_arr,speech_arr):
        if face_score[0] == speech_score[0]:
            if face_score[1] != speech_score [1]:
                emotion_score.append([face_score[0],face_score[1]/2 + speech_score [1]/2])
            else:
                emotion_score.append(face_score)
            emotions.append(face_score[0])
        elif face_score[1]>speech_score[1]:
            emotion_score.append(face_score)
            emotions.append(face_score[0])
        else:
            emotion_score.append(speech_score)
            emotions.append(speech_score[0])


    emotion_dict = {0:'angry', 1:'disgust', 2:'fear', 3:'happy', 4:'sad', 5:'surprise', 6:'neutral'}

    classification = {0:'depression' ,1: 'did',2:'bipolar',3:'anxiety',4:'schizophrenia' ,5:'ocd',6:'ptsd',7:'adhd' ,8:'Suicide' ,9:'postpartum' ,10:'pmdd',11:'None'}


    classification = {v: k for k, v in classification.items()}

    emotion_relation = {0:['sad','disgust'] ,1:['sad','disgust','neutral','surprise'],2:['sad','disgust','neutral','fear'],
                        3:['sad','disgust'] , 4:['fear','disgust','neutral'] ,5:['fear','sad','disgust'],6:['fear','sad'],
                        7:['anger','disgust','surprise'],8:['sad','angry'] ,9:['sad','angry','fear'],10:['sad','angry'],11:['None']}

    if classification[quest_arr] == 11:
        verdict = True
    else:
        related_emotions = emotion_relation[classification[quest_arr]]
        print(emotions)
        print(related_emotions)
        inter = [value for value in emotions if value in related_emotions]
        print('INTER', inter)
        if len(inter) >= 1:
            verdict = True
        else:
            verdict = False

    Activation = 0
    Pleasantness = 0
    Score = 0
    for emotion in emotion_score:
        if emotion[0] in ['happy', 'sad', 'angry', 'neutral']:
            activation, pleasantness = multi_dimension_emotion(emotion)
            Activation += activation
            Pleasantness += pleasantness
    Activation = Activation / len(emotion_score)
    Pleasantness = Pleasantness / len(emotion_score)

    if Activation >= 70 and Pleasantness >= 70:
        score = 100
    elif Activation >= 60 and Pleasantness >= 60:
        score = 75
    elif Activation >= 40 and Pleasantness >= 40:
        score = 50
    elif Activation >= 20 and Pleasantness >= 20:
        score = 25
    else:
        score = 10

    return score,verdict

def multi_dimension_emotion(parameters):
    [emotion, confidence] = parameters
    if emotion == 'happy':
        activation = (confidence * (83 - 51)) + 51
        pleasantness = (confidence * (86 - 50)) +50
    elif emotion == 'sad':
        activation = (confidence * (67 - 16)) + 16
        pleasantness = (confidence * (54 - 19)) + 19
    elif emotion == 'angry':
        activation = (confidence * (83 - 51)) + 51
        pleasantness = (confidence * (51 - 13)) + 13
    elif emotion == 'neutral':
        activation = (confidence * (68 - 19)) + 19
        pleasantness = (confidence * (51 - 13)) + 13

    return (activation,pleasantness)


face_arr =  [['neutral' ,0.7],['happy',0.9]]
speech_arr =  [['neutral', 0.8], ['happy', 0.8]]
quest_arr = 'did'
print(score_calc(face_arr,speech_arr,quest_arr))



