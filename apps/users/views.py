import random

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from freshshop.settings import APIKEY
from apps.users.models import VerifyCode
from apps.users.serializers import SmsSerializer
from apps.utils.yunpian import YunPian

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


class SmsCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    手机验证码
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        sms_code = '%06d' % random.randint(0, 999999)
        return str(sms_code)

    def create(self, request, *args, **kwargs):
        """
        重写create方法
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        # 验证是否合法
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        # 获取云片对象,用于发送短信
        yun_pian = YunPian(APIKEY)
        # 生成验证码
        code = self.generate_code()
        # 发送短信
        sms_status = yun_pian.send_sms(code, mobile)
        if sms_status['code'] != 0:
            return Response({
                "mobile": sms_status['msg']
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                'mobile': mobile
            }, status=status.HTTP_201_CREATED)
