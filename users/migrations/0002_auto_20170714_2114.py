# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 18:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traineeinfo',
            name='address',
            field=models.CharField(max_length=150, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='traineeinfo',
            name='birth_date',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='traineeinfo',
            name='dsc',
            field=models.TextField(max_length=2000, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='traineeinfo',
            name='education',
            field=models.CharField(max_length=150, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='traineeinfo',
            name='f',
            field=models.CharField(max_length=30, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='traineeinfo',
            name='i',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='traineeinfo',
            name='o',
            field=models.CharField(max_length=30, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='traineeinfo',
            name='phone',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+79001234567' or '89001234567'", regex='^(\\+7)|8\\d{10}$')], verbose_name='Телефон'),
        ),
    ]
