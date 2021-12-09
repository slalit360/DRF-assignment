from .serializers import *
import logging
from django.contrib.auth.models import Group
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from account.models import User
from rest_framework_simplejwt.tokens import RefreshToken

logger = logging.getLogger(__name__)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterUser(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = RegisterUserSerializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                user = User(**serializer.data)
                if user:
                    group = Group.objects.filter(name__exact='Users').first()
                    user_db = User.objects.get(id=user.id)
                    user_db.groups.add(group)
                    user_db.save()
                    return_data = UserSerializers(user).data
                    return_data['token'] = get_tokens_for_user(user)
                    response = Response(return_data, status=status.HTTP_201_CREATED)
                    return response
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(e.__cause__)
            logger.error(e)
            return Response({"message": e.__cause__}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserLogin(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = UserLoginSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.instance
                request.user = user
                user.last_login = timezone.now()
                user.save()
                user_ser = UserSerializers(user, many=False)
                ret_data = user_ser.data
                ret_data['token'] = get_tokens_for_user(user)
                resp = Response(ret_data, status=status.HTTP_200_OK)
                return resp
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(e.__cause__)
            logger.error(e)
            return Response({"message": e.__cause__}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
