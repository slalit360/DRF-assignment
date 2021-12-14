from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import *
from .serializers import *
import logging

logger = logging.getLogger(__name__)


class QueryAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = QuerySerializer
    queryset = Query.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            request.data['user'] = request.user.id
            serializer = QuerySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=request.user.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(e, e.__cause__)
            return Response({"message": e.__cause__}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AnswerAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsMentor]
    authentication_classes = [JWTAuthentication]
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            serializer = AnswerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(answered_by=request.user)
                return Response({"message": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(e, e.__cause__)
            return Response({"message": e.__cause__}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
