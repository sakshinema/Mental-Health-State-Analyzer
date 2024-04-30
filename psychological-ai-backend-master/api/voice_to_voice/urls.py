from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClassifyView.as_view()),
    path('diagnose/', views.DiagnoseView.as_view()),
    path('getSeverity/', views.GetSeverityView.as_view()),
    path('saveHistory/', views.SaveHistoryView.as_view()),
    path('getHistory/', views.ViewHistoryView.as_view()),
    path('getRecommendations/', views.GetRecommendationsView.as_view()),
    path('getOverallScore/', views.OverallScoreView.as_view()),
]
