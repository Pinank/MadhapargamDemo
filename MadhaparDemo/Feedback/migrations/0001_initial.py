# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gamuser', '0003_auto_20160909_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback_subject', models.CharField(max_length=20, verbose_name='Subject')),
                ('feedback_description', models.TextField(max_length=2000)),
                ('feedback_date', models.DateField(auto_now=True, verbose_name='Date')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamuser.UserInfo', verbose_name='User Name')),
            ],
        ),
    ]