# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-19 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_auto_20190329_1233'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAsk',
        ),
        migrations.DeleteModel(
            name='UserMessage',
        ),
    ]