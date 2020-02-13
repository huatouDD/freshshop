__author__ = 'jayyywah'

import xadmin
from xadmin import views
from apps.users.models import VerifyCode


class BaseSetting(object):
    """
    添加主题功能
    """
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    # 全局配置, 后台管理标题页脚
    site_title = "钢之炼金术师"
    site_footer = "www.baidu.com"

    # 菜单收缩
    menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)