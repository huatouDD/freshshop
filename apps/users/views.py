from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户认证： 用户名和电话一样可以登录
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        重写此方法
        :param request:
        :param username:
        :param password:
        :param kwargs:
        :return:
        """
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None
