from django.urls import path
from . import views

urlpatterns = [
    path('summarizer', views.summarize, name='summarizer'),
]