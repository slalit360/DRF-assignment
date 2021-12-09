from django.urls import path
from .views import *

urlpatterns = [
    path(r'query/', QueryView.as_view(), name="new-query"),
    path(r'answer/', AnswerView.as_view(), name="answer-query"),
]

# from rest_framework import routers
# router = routers.SimpleRouter()
# router.register(r'query', QueryView)
# router.register(r'answer', AnswerView)
# urlpatterns += router.urls