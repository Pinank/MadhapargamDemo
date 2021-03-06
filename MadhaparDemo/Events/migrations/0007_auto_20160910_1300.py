# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 13:00
from __future__ import unicode_literals

import Events.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0006_auto_20160909_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventalbum',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='eventalbum',
            name='width_field',
        ),
        migrations.AddField(
            model_name='eventalbum',
            name='event_photo_created_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='eventalbum',
            name='event_photo_updated_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='eventstatusofuser',
            name='event_status_created_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='eventalbum',
            name='event_photo',
            field=models.ImageField(default=1, upload_to=Events.models.upload_location, verbose_name='Event Photo'),
            preserve_default=False,
        ),
    ]
