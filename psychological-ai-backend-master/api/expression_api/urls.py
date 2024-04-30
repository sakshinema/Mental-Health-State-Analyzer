from django.http import StreamingHttpResponse
from django.urls import path

from expression_api.camera import VideoCamera, gen

urlpatterns = [
    path('', lambda r: StreamingHttpResponse(gen(VideoCamera()),
                                                     content_type='multipart/x-mixed-replace; boundary=frame')),

]
