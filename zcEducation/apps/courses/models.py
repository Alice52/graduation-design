from django.db import models
from datetime import datetime
from orgs.models import OrgsInfo, TeacherInfo


# Create your models here.
class CourseInfo(models.Model):
    image = models.ImageField(upload_to='course/', max_length=200, verbose_name='课程封面')
    name = models.CharField(verbose_name='课程名称', max_length=20)
    study_time = models.IntegerField(verbose_name='课程时长', default=0)
    study_num = models.IntegerField(verbose_name='学习人数', default=0)
    level = models.CharField(choices=(('gj', '高级'), ('zj', '中级'), ('cj', '初级')), verbose_name='课程难度', max_length=5,
                             default='cj')
    love_num = models.IntegerField(verbose_name='收藏数', default=0)
    click_num = models.IntegerField(verbose_name='点击数量', default=0)
    desc = models.CharField(verbose_name='课程简介', max_length=200)
    detail = models.CharField(verbose_name='课程详情',  max_length=300)
    category = models.CharField(choices=(('qd', '前端开发'), ('hd', '后端开发')), verbose_name='课程类别', max_length=5)
    course_notice = models.CharField(verbose_name='课程公告', max_length=200)
    course_need = models.CharField(verbose_name='课程须知', max_length=200)
    teacher_tell = models.CharField(verbose_name="讲师提示", max_length=200)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    orginfo = models.ForeignKey(OrgsInfo, verbose_name='所属机构', on_delete=models.CASCADE)
    teacherinfo = models.ForeignKey(TeacherInfo, verbose_name='所属讲师', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name


class LessonInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name="章节名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    courseinfo = models.ForeignKey(CourseInfo, verbose_name="所属课程", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name


class VideoInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name="视频名称")
    study_time = models.IntegerField(default=0, verbose_name="视频时长")
    url = models.URLField(default='http://www.atguigu.com', verbose_name="视频链接", max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    lessoninfo = models.ForeignKey(LessonInfo, verbose_name="所属章节", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '视频信息'
        verbose_name_plural = verbose_name


class SourceInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name="资源名称")
    down_load = models.FileField(upload_to='source/', max_length=200, verbose_name="下载路径")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    courseinfo = models.ForeignKey(CourseInfo, verbose_name="所属课程", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '资源信息'
        verbose_name_plural = verbose_name
