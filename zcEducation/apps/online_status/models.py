# from django.db import models
# from zcEducation import settings
# from django.core.cache import cache
# import datetime
# from django.utils import timezone
# # Create your models here.
#
# class OnlineStatus(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     last_login = models.DateTimeField(default=timezone.now)
#     class Meta:
#         verbose_name = 'Online Status'
#         verbose_name_plural = 'Online Status'
#         ordering = ['-last_login']
#
#     def __str__(self):
#         return '%s last login at UTC %s' % (self.user.username, self.last_login.strftime('%Y/%m/%d %H:%M'))
#
#     def get_last_active(self):
#         cache_key = '%s_last_login' % self.user.username
#         # 如果缓存过期，从数据库获取last_login，并存到缓存
#         if not cache.get(cache_key):
#             print("####### index view -- cache not found")
#             cache.set(cache_key, self.last_login, settings.USER_LAST_LOGIN_EXPIRE)
#         return cache.get(cache_key)
#
#     def is_online(self):
#         now = timezone.now()
#         if self.get_last_active() < now - datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT):
#             return False
#         return True
from django.db import models
from datetime import datetime
from users.models import UserProfile
from courses.models import CourseInfo


class UserRecord(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    cour_id = models.IntegerField(verbose_name="课程ID", default=0)
    # course = models.ForeignKey(CourseInfo, verbose_name="课程", on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name="登录或开始时间", default=None, null=True)
    end_time = models.DateTimeField(verbose_name="推出或结束时间", default=None, null=True)
    month = models.IntegerField(verbose_name="月份", default=None, null=True)
    # 1: 表示为 login/logout; 2: 表示为 course 的学习
    type = models.IntegerField(verbose_name="类型", default=1)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '用户行为记录信息'
        verbose_name_plural = verbose_name
