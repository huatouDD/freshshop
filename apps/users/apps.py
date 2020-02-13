from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'apps.users'
    # 在后台管理系统中设置中文
    verbose_name = "用户管理"
