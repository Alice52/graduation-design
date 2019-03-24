from django.db import models
from datetime import datetime


# Create your models here.
class CityInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市名称')
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '城市信息'
        verbose_name_plural = verbose_name


class OrgsInfo(models.Model):
    image = models.ImageField(upload_to='org/', max_length=200, verbose_name='机构封面')
    name = models.CharField(max_length=20, verbose_name='机构名称')
    course_num = models.IntegerField(verbose_name='课程数', default=0)
    study_num = models.IntegerField(verbose_name='学习人数', default=0)
    address = models.CharField(max_length=200, verbose_name='机构地址')
    desc = models.CharField(max_length=200, verbose_name='机构简介')
    detail = models.CharField(verbose_name='机构详情', max_length=200)
    love_num = models.IntegerField(verbose_name='收藏数', default=0)
    click_num = models.IntegerField(verbose_name='点击数量', default=0)
    category = models.CharField(choices=(('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')), verbose_name='机构类别',
                                max_length=200)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    cityinfo = models.ForeignKey(CityInfo, verbose_name='所属城市', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '机构信息'
        verbose_name_plural = verbose_name


class TeacherInfo(models.Model):
    image = models.ImageField(upload_to='teacher/', max_length=200, verbose_name='讲师头像')
    name = models.CharField(verbose_name='讲师姓名', max_length=20)
    work_year = models.IntegerField(verbose_name='工作年限', default=3)
    work_position = models.CharField(verbose_name='工作职位', max_length=20)
    work_style = models.CharField(verbose_name='教学特点', max_length=20)
    age = models.IntegerField(verbose_name='讲师年龄', default=30)
    gender = models.CharField(choices=(('girl', '女'), ('boy', '男')), max_length=10, verbose_name='讲师性别', default='girl')
    love_num = models.IntegerField(verbose_name='收藏数', default=0)
    click_num = models.IntegerField(verbose_name='点击数量', default=0)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    work_company = models.ForeignKey(OrgsInfo, verbose_name='所属机构', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '讲师信息'
        verbose_name_plural = verbose_name
