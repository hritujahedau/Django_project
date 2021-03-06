# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-19 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='DataInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_info_type', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.TimeField(blank=True, null=True)),
                ('updated_time', models.TimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PostLikeDisLikeByPeople',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('_type', models.CharField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agro.Post')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('profile_pic_url', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(max_length=10)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agro.Location')),
            ],
        ),
        migrations.AddField(
            model_name='postlikedislikebypeople',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agro.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agro.User'),
        ),
        migrations.AddField(
            model_name='datainfo',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agro.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agro.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agro.User'),
        ),
    ]
