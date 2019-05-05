from datetime import datetime
from django.core.cache import cache
from zcEducation import settings
from .models import UserRecord
from django.utils.deprecation import MiddlewareMixin


class OnlineStatusMiddleware(MiddlewareMixin):

    # def process_request(self, request):
    #     if request.user.is_authenticated():
    #         cache_key = '%s_last_login' % request.user.username
    #         now = datetime.now()
    #         userrecord = UserRecord.objects.filter(user=request.user).order_by('-start_time')
    #         # 用户是第一次登录、或者是缓存过去、或者是服务器重启导致缓存消失
    #         if not cache.get(cache_key):
    #             print('#### cache not found #####')
    #             if not userrecord:
    #                 ur = UserRecord()
    #                 ur.user = request.user
    #                 ur.month = now.month
    #                 ur.start_time = now
    #                 ur.save()
    #             else:
    #                 ur = userrecord[0]
    #                 if ur.end_time:
    #                     ur = UserRecord()
    #                     ur.user = request.user
    #                     ur.month = now.month
    #                     ur.start_time = now
    #                     ur.save()
    #                 else:
    #                     ur.end_time = now
    #                     ur.save()
    #
    #             cache.set(cache_key, now, settings.USER_LAST_LOGIN_EXPIRE)
    #
    #         else:
    #             print("##### cache found ######")
    #             if 'user_logout' in request.path:
    #                 ur = userrecord[0]
    #                 if not ur.end_time:
    #                     ur.end_time = now
    #                     ur.save()
    #             if 'get_user' in request.path:
    #                 ur = UserRecord()
    #                 ur.user = request.user
    #                 ur.month = now.month
    #                 ur.start_time = now
    #                 ur.save()
    #             cache.set(cache_key, now, settings.USER_LAST_LOGIN_EXPIRE)
    def process_request(self, request):
        if request.user.is_authenticated():
            now = datetime.now()
            userrecord = UserRecord.objects.filter(user=request.user).order_by('-start_time')
            if not userrecord:
                ur = UserRecord()
                ur.user = request.user
                ur.month = now.month
                ur.start_time = now
                ur.save()
            elif 'get_user' in request.path:  # F5
                ur = userrecord[0]
                if not ur.end_time:
                    pass
                else:
                    ur = UserRecord()
                    ur.user = request.user
                    ur.month = now.month
                    ur.start_time = now
                    ur.save()
            elif 'user_logout' in request.path:  # 长时间无操作 默认退出
                ur = userrecord[0]
                ur.end_time = now
                ur.save()

        return None
