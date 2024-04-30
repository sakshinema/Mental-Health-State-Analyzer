from django.contrib.auth.models import User

# Create your views here.
from rest_framework import views
from rest_framework.response import Response

from .serializers import EmotionSerializer

from expression_api.camera import VideoCamera, gen


class EmotionView(views.APIView):

    def get(self, request):
        t = gen(VideoCamera())
        print(t)
        res = {}

        if t:
            data_file = open("E:\\projects\\psychological-ai-backend\\api\\expression_api\\emotion_logs.txt", 'r')
            data = data_file.readlines()

            for i in range(len(data)):
                res[i] = data[i][:-1]

            print('dataz',res)
        # results = EmotionSerializer(data, many=True).data
        return Response(res)
