# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-18 16:01
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2018, 9, 18, 16, 1, 58, 905212))),
                ('modifiedAt', models.DateTimeField(default=datetime.datetime(2018, 9, 18, 16, 1, 58, 905256))),
                ('authorName', models.CharField(max_length=60)),
                ('authorEmail', models.EmailField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2018, 9, 18, 16, 1, 58, 905212))),
                ('modifiedAt', models.DateTimeField(default=datetime.datetime(2018, 9, 18, 16, 1, 58, 905256))),
                ('bookId', models.CharField(max_length=30)),
                ('bookName', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
