from django.urls import path
from .views import *

urlpatterns = [
    path(r'query/', QueryAPIView.as_view(), name="new-query"),
    path(r'answer/', AnswerAPIView.as_view(), name="answer-query"),
]

# from rest_framework import routers
# router = routers.SimpleRouter()
# router.register(r'query', QueryView)
# router.register(r'answer', AnswerView)
# urlpatterns += router.urls