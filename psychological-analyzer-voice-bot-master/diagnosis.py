from gtts import gTTS  
from playsound import playsound 
from time import sleep
import speech_recognition as sr
import pyttsx3,os,requests
import wavio as wv
import disorder,json


def play(text):
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



#loading classification dataset
def load(fname):
    import json
    name = 'data/'+fname+'.json'
    with open(name) as f:
        res = json.load(f)
    return res

def classify(fname):
    tests = []
    hurestic = {
    "anxiety":[0,9],
    "ocd":[0,7],
    "depression":[0,8],
    "did":[0,6],
    "suicidal":[0,2],
    "ptsd":[0,4],
    "schizophrenia":[0,5],
    "adhd":[0,5],
    "postpartum":[0,5],
    "bipolar":[0,8],
    "pmdd":[0,8]
    }
    r = sr.Recognizer() 
    classify = load("classify")
    play('listen carefully and speak up the most suitable option clearly and loudly.')
    for k,v in classify.items():
        play(k)
        play('options are:')
        for x in v:
            play(x[0])
        while(1):   
            try:
                with sr.Microphone() as source2:
                    r.adjust_for_ambient_noise(source2, duration=1)
                    #print('Recording...')
                    play('Recording')

                    audio2 = r.listen(source2)
                    name = '_'.join(k.split())

                    with open('recording/classify/'+name+'.wav','wb') as f:
                        f.write(audio2.get_wav_data())

                    play('Recorded')
                    print()
                    
                    text = r.recognize_google(audio2)
                    text = text.lower()
                    print(text)
                    for x in v:
                        try:
                            if x[0].lower() in text.lower():
                                for i in range(1,len(x)):
                                    n,key = x[i][0],x[i][1:]
                                    print(n,key)
                                    hurestic[key.lower()][0] += int(n)
                        except:pass
                    break
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                
            except sr.UnknownValueError:
                print("unknown error occured")

        sleep(3)
        #break

    #getting hurestic test result
    for k,v in hurestic.items():
        if v[0]*100/v[1] > 60:
            tests.append(k)
    print(tests)
    return {"tests" : " ".join(tests)}



#actual tests
def diagnose(tests_str):
    test_result = {}
    tests = tests_str.split()
    r = sr.Recognizer() 
    r.energy_threshold = 40
    for test in tests:
        ques = load(test)

        play('listen carefully and speak up the most suitable option clearly and loudly.')
        for k,v in ques.items():
            play(k)
            play('options are:')
            for x in v:
                play(x[0])
            while(1):   
                try:
                    with sr.Microphone() as source2:
                        r.adjust_for_ambient_noise(source2, duration=1)
                        #print('Recording...')
                        play('Recording')

                        audio2 = r.listen(source2)
                        name = '_'.join(k.split())
                        with open('recording/'+test+'/'+name+'.wav','wb') as f:
                            f.write(audio2.get_wav_data())
                        
                        play('Recorded')
                        print()
                        
                        text = r.recognize_google(audio2)
                        text = text.lower()
                        print(text)
                        for x in v:
                            if x[0].lower() in text.lower():
                                if test in test_result:
                                    test_result[test] += int(x[1])
                                else:test_result[test] = int(x[1])

                        break
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))
                    
                except sr.UnknownValueError:
                    print("unknown error occured. Please say you answer again.")
            
            sleep(3)
            #break
    out_file = open("test-result.json", "w") 
    json.dump(test_result, out_file, indent = 4) 
    out_file.close()
    return test_result


def get_severity(test_result):
    severity = {}
    for k,v in test_result.items():
        if k.lower() == 'adhd':
            severity[k] = disorder.adhd(v)
        elif k.lower() == 'anxiety':
            severity[k] = disorder.anxiety(v)
        elif k.lower() == 'bipolar':
            severity[k] = disorder.bipolar(v)
        elif k.lower() == 'depression':
            severity[k] = disorder.depression(v)
        elif k.lower() == 'did':
            severity[k] = disorder.did(v)
        elif k.lower() == 'ocd':
            severity[k] = disorder.ocd(v)
        elif k.lower() == 'pmdd':
            severity[k] = disorder.pmdd(v)
        elif k.lower() == 'postpartum':
            severity[k] = disorder.postpartum(v)
        elif k.lower() == 'ptsd':
            severity[k] = disorder.ptsd(v)
        elif k.lower() == 'schizophrenia':
            severity[k] = disorder.schizophrenia(v)
        elif k.lower() == 'suicidal':
            severity[k] = disorder.suicidal(v)

    out_file = open("disease_severity.json", "w") 
    json.dump(severity, out_file, indent = 4) 
    out_file.close()
    return severity

def save_history(user_id,disease_score):
    #user_id = "rahul0405"

    import pymongo
    client = pymongo.MongoClient("mongodb+srv://rahul:rahul@mentalhealthstatusanaly.5wzql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    database = client[user_id]
    collection = database['history']

    import datetime
    time = datetime.datetime.now()
    timestamp = time.timestamp()
    
    data = {str(timestamp):disease_score}
    collection.insert_one(data)
    return {"result":"history saved for user {}".format(user_id)}

def view_history(user_id):
    #user_id = "rahul0405"
    import pymongo
    from datetime import datetime
    client = pymongo.MongoClient("mongodb+srv://rahul:rahul@mentalhealthstatusanaly.5wzql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    database = client[user_id]
    collection = database['history']
    
    records = collection.find({})
    result = {}
    for document in records:
        for k,v in document.items():
            if k =='_id': continue
            k = int(float(k))
            key = datetime.fromtimestamp(k)
            result[str(key)] = v

    return {user_id:result}