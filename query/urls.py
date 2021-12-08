from django.urls import path
from .views import *

urlpatterns = [
    path(r'new-query/', QueryView.as_view(), name="new-query"),
    path(r'answer-query/', AnswerQueryView.as_view(), name="answer-query"),
]