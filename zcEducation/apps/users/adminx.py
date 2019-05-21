import xadmin
from .models import BannerInfo, EmailVerifyCode
from xadmin import views


# 配置xadmin主题,注册的时候要用到专用的view去注册
class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True


class CommXadminSetting(object):
    site_title = 'zc在线教育后台管理系统'
    site_footer = '617室 ZC在线学习平台'
    menu_style = 'accordion'


class BannerInfoXadmin(object):
    list_display = ['image', 'url', 'add_time']
    search_fields = ['image', 'url']
    list_filter = ['image', 'url']


xadmin.site.register(BannerInfo, BannerInfoXadmin)
# 注册主题类
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
# 注册全局样式的类
xadmin.site.register(views.CommAdminView, CommXadminSetting)
