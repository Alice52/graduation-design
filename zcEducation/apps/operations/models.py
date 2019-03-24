from django.db import models
from datetime import datetime
from users.models import UserProfile
from courses.models import CourseInfo


# Create your models here.
class UserAsk(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20)
    phone = models.CharField(verbose_name='手机号', max_length=11)
    course = models.CharField(verbose_name='课程', max_length=20)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name


class UserLove(models.Model):
    love_id = models.IntegerField(verbose_name='收藏的ID')
    love_type = models.IntegerField(verbose_name='收藏类型', choices=((1, 'org'), (2, 'course'), (3, 'teacher')))
    love_status = models.BooleanField(verbose_name='收藏状态', default=False)
    add_time = models.DateTimeField(verbose_name='收藏时间', default=datetime.now)
    love_man = models.ForeignKey(UserProfile, verbose_name='收藏用户', on_delete=models.CASCADE)

    def __str__(self):
        return self.love_man.username

    class Meta:
        verbose_name = '收藏信息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    add_time = models.DateTimeField(verbose_name='收藏时间', default=datetime.now)
    study_man = models.ForeignKey(UserProfile, verbose_name='学习用户', on_delete=models.CASCADE)
    study_course = models.ForeignKey(CourseInfo, verbose_name='学习课程', on_delete=models.CASCADE)

    def __str__(self):
        return self.study_man.username

    class Meta:
        unique_together = ('study_man', 'study_course')
        verbose_name = '用户学习课程信息'
        verbose_name_plural = verbose_name


class UserComment(models.Model):
    comment_content = models.CharField(verbose_name='评论内容', max_length=300)
    add_time = models.DateTimeField(verbose_name='评论时间', default=datetime.now)
    comment_man = models.ForeignKey(UserProfile, verbose_name='评论用户', on_delete=models.CASCADE)
    comment_course = models.ForeignKey(CourseInfo, verbose_name='评论课程', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_man.username

    class Meta:
        verbose_name = '评论信息'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    message_man = models.IntegerField(verbose_name='消息用户', default=0)
    message_content = models.CharField(verbose_name='消息内容', max_length=200)
    message_status = models.BooleanField(verbose_name='消息状态', default=False)
    add_time = models.DateTimeField(verbose_name='消息时间', default=datetime.now)

    def __str__(self):
        return self.message_content

    class Meta:
        verbose_name = '用户消息信息'
        verbose_name_plural = verbose_name
