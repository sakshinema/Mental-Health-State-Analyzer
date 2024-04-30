from django.urls import path

from . import views

urlpatterns = [
    path('emotion/', views.EmotionView.as_view()),
]
