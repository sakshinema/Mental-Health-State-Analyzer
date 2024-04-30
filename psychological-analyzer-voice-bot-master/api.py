from fastapi import FastAPI, File, UploadFile
import shutil
from typing import Optional
from pydantic import BaseModel
import diagnosis

class Result(BaseModel):
    anxiety: Optional[int] = None
    ocd: Optional[int] = None
    depression: Optional[int] = None
    did: Optional[int] = None
    suicidal: Optional[int] = None
    ptsd: Optional[int] = None
    schizophrenia: Optional[int] = None
    adhd: Optional[int] = None
    postpartum: Optional[int] = None
    bipolar: Optional[int] = None
    pmdd: Optional[int] = None

app = FastAPI()


@app.get("/classify/")
def send_classify():
    return diagnosis.classify("classify")


@app.get("/diagnose/{tests}/")
def diagnose(tests : str):
    return diagnosis.diagnose(tests)


@app.post("/get-severity/")
def get_severity(result:Result):
    test_result = {}

    if result.anxiety != None: test_result['anxiety'] = result.anxiety
    if result.ocd != None: test_result['ocd'] = result.ocd
    if result.depression != None: test_result['depression'] = result.depression
    if result.did != None: test_result['did'] = result.did
    if result.suicidal != None: test_result['suicidal'] = result.suicidal
    if result.ptsd != None: test_result['ptsd'] = result.ptsd
    if result.schizophrenia != None: test_result['schizophrenia'] = result.schizophrenia
    if result.adhd != None: test_result['adhd'] = result.adhd
    if result.postpartum != None: test_result['postpartum'] = result.postpartum
    if result.bipolar != None: test_result['bipolar'] = result.bipolar
    if result.pmdd != None: test_result['pmdd'] = result.pmdd
   
    return diagnosis.get_severity(test_result)


@app.post("/recommand/")
def get_recommendation(data):
    d = {}
    for name in data.keys():
        with open("/recommendations/"+name+".txt","r") as f:
            content = f.read()
        d[name] = content
    return d



'''
data = {user_id:disease_score}
'''
@app.post('/save_history/')
def save_history(data):
    return diagnosis.save_history(data.key(),data.value())

@app.get('/view_history/{user_id}')
def view_history(user_id:str):
    res = diagnosis.view_history(user_id)
    res = list(res)
    return {user_id:res}