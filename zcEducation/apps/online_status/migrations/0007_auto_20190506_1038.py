# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-06 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_status', '0006_auto_20190506_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrecord',
            name='data_id',
            field=models.IntegerField(default=None, null=True, verbose_name='课程ID'),
        ),
    ]
