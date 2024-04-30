import pymongo
from fastapi import FastAPI, File, UploadFile
import shutil
from typing import Optional
from pydantic import BaseModel
from voice_to_voice import diagnosis
from voice_to_voice import score

from rest_framework import views
from rest_framework.response import Response


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


class ClassifyView(views.APIView):
    def get(self, request):
        return Response(diagnosis.classify("classify"))


class DiagnoseView(views.APIView):
    def post(self, request):
        tests_str = request.data
        print('test string',tests_str)
        return Response(diagnosis.diagnose(tests_str["tests"]))


class GetSeverityView(views.APIView):
    def post(self, request):
        print(request.data, 'severrrrrrrrr')
        result = request.data

        # if result.anxiety != None: test_result['anxiety'] = result.anxiety
        # if result.ocd != None: test_result['ocd'] = result.ocd
        # if result.depression != None: test_result['depression'] = result.depression
        # if result.did != None: test_result['did'] = result.did
        # if result.suicidal != None: test_result['suicidal'] = result.suicidal
        # if result.ptsd != None: test_result['ptsd'] = result.ptsd
        # if result.schizophrenia != None: test_result['schizophrenia'] = result.schizophrenia
        # if result.adhd != None: test_result['adhd'] = result.adhd
        # if result.postpartum != None: test_result['postpartum'] = result.postpartum
        # if result.bipolar != None: test_result['bipolar'] = result.bipolar
        # if result.pmdd != None: test_result['pmdd'] = result.pmdd

        return Response(diagnosis.get_severity(result))


class SaveHistoryView(views.APIView):
    def post(self, request):
        data = {"test123": request.data}
        print('the data',data)
        return Response(diagnosis.save_history((list(data.keys()))[0], (list(data.values()))[0]))


class GetRecommendationsView(views.APIView):
    def post(self, request):
        data = request.data
        d = {}
        for name in data.keys():
            with open("E:\projects\psychological-ai-backend\\api\\voice_to_voice\\recommendations\\" + name + ".txt",
                      "r") as f:
                content = f.read()
            d[name] = content
        return Response(d)


class ViewHistoryView(views.APIView):
    def get(self, request):
        client = pymongo.MongoClient(
            "mongodb+srv://rahul:rahul@mentalhealthstatusanaly.5wzql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        database = client["test123"]
        collection = database['history']

        records = collection.find({})
        result = {}
        from datetime import datetime
        for document in records:
            for k, v in document.items():
                if k == '_id': continue
                k = int(float(k))
                key=datetime.fromtimestamp(k)
                result[str(key)] = v

        return Response({"rahul": result})


class OverallScoreView(views.APIView):
    def post(self, request):
        data = request.data

        print(data,'this is the data')

        temp = []
        for it in data['faceArr']:
            temp.append([it[0], float(it[1])])

        temp2 = []

        for emo in data["speechArr"]["Emotion"]:
            temp2.append([emo, float(data["speechArr"]["Severity"])])



        print('VARIABLESSSSSSSS', temp2)
        res = score.score_calc(temp,
                               temp2,
                               'anxiety')
        scr, verdict = res
        return Response({"score":scr, "verdict":verdict})
