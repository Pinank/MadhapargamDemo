# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0007_auto_20160910_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventstatusofuser',
            name='event_status_updated_date',
            field=models.DateField(auto_now=True),
        ),
    ]
