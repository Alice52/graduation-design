# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-05 14:18
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0003_auto_20190505_1418'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='登录或开始时间')),
                ('end_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='推出或结束时间')),
                ('month', models.IntegerField(default=5, verbose_name='月份')),
                ('type', models.IntegerField(default=1, verbose_name='类型')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseInfo', verbose_name='课程')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户行为记录信息',
                'verbose_name_plural': '用户行为记录信息',
            },
        ),
    ]
