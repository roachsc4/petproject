# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 13:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specs', '0002_auto_20170619_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='iframe_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='trainee',
            field=models.ManyToManyField(blank=True, through='specs.TraineeLesson', to=settings.AUTH_USER_MODEL),
        ),
    ]
