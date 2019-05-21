from django.db import models
from datetime import datetime
from users.models import UserProfile
from courses.models import CourseInfo



class UserLove(models.Model):
    love_man = models.ForeignKey(UserProfile, verbose_name="收藏用户", on_delete=models.CASCADE)
    love_id = models.IntegerField(verbose_name="收藏id")
    love_type = models.IntegerField(choices=((1, '机构'), (2, '课程'), (3, '讲师')), verbose_name="收藏类别")
    love_status = models.BooleanField(default=False, verbose_name="收藏状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="收藏时间")

    def __str__(self):
        return self.love_man.username

    class Meta:
        verbose_name = '收藏信息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    study_man = models.ForeignKey(UserProfile, verbose_name="学习用户", on_delete=models.CASCADE)
    study_course = models.ForeignKey(CourseInfo, verbose_name="学习课程", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="学习时间")

    def __str__(self):
        return self.study_man.username

    class Meta:
        unique_together = ('study_man', 'study_course')
        verbose_name = '用户学习课程信息'
        verbose_name_plural = verbose_name


class UserComment(models.Model):
    comment_man = models.ForeignKey(UserProfile, verbose_name="评论用户", on_delete=models.CASCADE)
    comment_course = models.ForeignKey(CourseInfo, verbose_name="评论课程", on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=300, verbose_name="评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="评论时间")

    def __str__(self):
        return self.comment_content

    class Meta:
        verbose_name = '用户评论课程信息'
        verbose_name_plural = verbose_name

