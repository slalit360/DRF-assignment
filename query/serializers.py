from rest_framework import serializers
from .models import *


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('id', 'title', 'description', 'file')


class AnswerQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuery
        fields = ('id', 'query', 'answer')
