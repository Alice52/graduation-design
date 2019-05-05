from django.db import models
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
