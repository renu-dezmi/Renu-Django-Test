# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-18 18:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Books', '0002_auto_20180918_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 18, 18, 14, 54, 533029)),
        ),
        migrations.AlterField(
            model_name='authors',
            name='modifiedAt',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 18, 18, 14, 54, 533076)),
        ),
    ]