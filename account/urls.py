from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)
from .views import *

urlpatterns = [
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterUser.as_view(), name="user-register"),
    path('login/', UserLogin.as_view(), name="user-login"),
    path('logout/', TokenBlacklistView.as_view(), name="user-logout"),
]


def create_default_user_group():
    group_names = ["Users", "Mentors"]
    try:
        for name in group_names:
            if not Group.objects.filter(name__exact=name).exists():
                group = Group(name=name)
                group.save()
    except:
        pass


create_default_user_group()
