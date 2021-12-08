from rest_framework import serializers
from .models import *


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'


class AnswerQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuery
        fields = '__all__'
