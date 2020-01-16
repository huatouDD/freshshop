import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

# Create your models here.

__author__ = 'jayyywah'


class UserProfile(AbstractUser):
    """
    用户详情
    """
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )  # xx.gender ==>>> "male" ; xx.get_gender_display ===>>u"男"
    # 用户基本信息
    name = models.CharField("姓名", max_length=30, null=True,
                            blank=True)  # null=True为可以为空，blank是针对表单的，True表示你的表单填写该字段的时候可以不填
    birthday = models.DateField("出生年月", null=True, blank=True)
    gender = models.CharField("性别", max_length=6, choices=GENDER_CHOICES, default="female")
    mobile = models.CharField("电话", max_length=11)  # 11个字节
    email = models.EmailField("邮箱", max_length=100, null=True, blank=True)

    class Meta:
        # 定义在管理后台显示的名称
        verbose_name = "用户信息"
        # 定义复数时的名称（去除复数的s）
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    """
    验证码
    """
    code = models.CharField("验证码", max_length=10)
    mobile = models.CharField("电话", max_length=11)
    add_time = models.DateTimeField("添加时间", default=now)  # 年月日时分秒

    class Meta:
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
