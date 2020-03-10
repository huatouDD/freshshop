import datetime
import re

from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.users.models import VerifyCode

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    """
    短信序列化器
    """
    mobile = serializers.CharField(max_length=11)

    # 函数必须：validate + 验证字段名
    def validate_mobile(self, mobile):
        """
        手机号码验证
        :param mobile:
        :return:
        """
        if User.objects.filter(mobile=mobile):
            raise serializers.ValidationError("用户已注册")

        if not re.match("^1[35678]\d{9}$", mobile):
            raise serializers.ValidationError("手机不合法")

        # 验证码发送频率
        # 60秒只能发送一次
        one_mins_ago = datetime.datetime.now() - datetime.timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mins_ago, mobile=mobile).count():
            raise serializers.ValidationError('发送频率过高！')

        return mobile
