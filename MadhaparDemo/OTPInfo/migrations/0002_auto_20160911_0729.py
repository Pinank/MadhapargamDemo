# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTPInfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='otp_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
