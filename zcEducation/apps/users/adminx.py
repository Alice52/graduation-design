import xadmin
from .models import BannerInfo, EmailVerifyCode
from xadmin import views


# 配置xadmin主题,注册的时候要用到专用的view去注册
class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True


class CommXadminSetting(object):
    site_title = 'zc在线学习后台管理系统'
    site_footer = 'zc教育617'
    menu_style = 'accordion'


class BannerInfoXadmin(object):
    # 显示内容
    list_display = ['image', 'url', 'add_time']
    # 搜索字段
    search_fields = ['image', 'url']
    # 筛选字段
    list_filter = ['image', 'url', 'add_time']


class EmailVerifyCodeXadmin(object):
    list_display = ['code', 'email', 'send_type', 'add_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'add_time']


xadmin.site.register(BannerInfo, BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeXadmin)
# 注册主题类
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
# 注册全局样式的类
xadmin.site.register(views.CommAdminView, CommXadminSetting)
