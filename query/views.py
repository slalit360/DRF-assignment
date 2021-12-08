from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import BasePermission
from .serializers import *
import logging

logger = logging.getLogger(__name__)


class UserOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_user():
            return True
        return False


class MentorOnly(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        if request.user.is_mentor():
            print("yes mentor")
            return True
        print("no mentor : user")
        return False


class QueryView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, UserOnly, MentorOnly]
    authentication_classes = [JWTAuthentication]
    serializer_class = QuerySerializer

    def post(self, request, *args, **kwargs):
        try:
            request.data['user'] = request.user.id
            serializer = QuerySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=request.user.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(e.__cause__)
            logger.error(e)
            return Response({"message": e.__cause__}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AnswerQueryView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, MentorOnly]
    authentication_classes = [JWTAuthentication]
    serializer_class = AnswerQuerySerializer

    def post(self, request, *args, **kwargs):
        try:
            print("Check mentor", request.user.is_mentor())
            print("Check User", request.user.is_user())

            serializer = AnswerQuerySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print("query answered")
                return Response({"message": serializer.data}, status=status.HTTP_201_CREATED)
            # print("answered error")
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # print("exception :", e)
            logger.error(e.__cause__)
            logger.error(e)
            return Response({"message": e.__cause__}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
