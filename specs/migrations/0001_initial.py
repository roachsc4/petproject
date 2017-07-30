# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 08:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_right', models.BooleanField()),
                ('score', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.SmallIntegerField(choices=[(1, 'Text'), (2, 'Image'), (3, 'Presentation'), (4, 'Video')])),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dsc', models.TextField(max_length=500)),
                ('iframe_link', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, max_length=2000, null=True)),
                ('type', models.SmallIntegerField(choices=[(1, 'One answer'), (2, 'Multiple answers'), (3, 'Free text answer')])),
                ('additional_params', django_mysql.models.JSONField(blank=True, default=dict, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('min_score', models.SmallIntegerField()),
                ('max_score', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='TraineeAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_params', django_mysql.models.JSONField(default=dict)),
                ('is_right', models.BooleanField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.Question')),
            ],
        ),
        migrations.CreateModel(
            name='TraineeLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Not passed'), (2, 'Passed')])),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.Lesson')),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TraineeTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(1, ' Not finished'), (2, 'Passed'), (3, 'Failed')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.Test')),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='traineeanswer',
            name='trainee_test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.TraineeTest'),
        ),
        migrations.AddField(
            model_name='test',
            name='trainee',
            field=models.ManyToManyField(through='specs.TraineeTest', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='spec',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.SpecType'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.Test'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.Spec'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='trainee',
            field=models.ManyToManyField(blank=True, through='specs.TraineeLesson', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attachment',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.Lesson'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.Question'),
        ),
    ]
