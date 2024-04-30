from gtts import gTTS  
from playsound import playsound 
from time import sleep
import speech_recognition as sr
import pyttsx3,os,requests
import wavio as wv

url='http://127.0.0.1:8000/upload'
get = 'http://127.0.0.1:8000/get'
test_res = 'http://127.0.0.1:8000/test-result'

def play(text):
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

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

classify = requests.get(get+'/classify/')
classify = classify.json()

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
                with open('tmp/'+name+'.wav','wb') as f:
                    f.write(audio2.get_wav_data())

                files = [('file',('tmp/'+name+".wav",open(name+'.wav','rb'),'wav'))]
                response = requests.post(url+'/classify/', files=files)
                print(response.json())
                play('Recorded')
                print()
                
                text = r.recognize_google(audio2)
                text = text.lower()
                print(text)
                for x in v:
                    try:
                        if x[0].lower() in text:
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


#actual tests
test_result = {}

for name in tests:
    ques = requests.get(get+'/'+name+'/')
    ques = ques.json()

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
                    with open('tmp/'+name+'.wav','wb') as f:
                        f.write(audio2.get_wav_data())

                    files = [('file',('tmp/'+name+".wav",open(name+'.wav','rb'),'wav'))]
                    response = requests.post(url+'/'+name+'/', files=files)
                    print(response.json())
                    play('Recorded')
                    print()
                    
                    text = r.recognize_google(audio2)
                    text = text.lower()
                    print(text)
                    for x in v:
                        if x[0].lower() in text:
                            if name in test_result:
                                test_result[name] += int(x[1])
                            else:test_result[name] = int(x[1])

                    break
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                
            except sr.UnknownValueError:
                print("unknown error occured")
        
        sleep(3)
        #break
requests.post(test_res,json=test_result)