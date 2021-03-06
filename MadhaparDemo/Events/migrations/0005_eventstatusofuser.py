# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 06:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamuser', '0002_auto_20160830_1043'),
        ('Events', '0004_auto_20160830_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventStatusOfUser',
            fields=[
                ('event_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_status_date', models.DateField(auto_now=True)),
                ('event_user_status', models.CharField(choices=[('1', 'Going'), ('2', 'Interested'), ('3', 'Maybe')], max_length=3)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.Event', verbose_name='Select Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamuser.UserInfo', verbose_name='Select User')),
            ],
        ),
    ]
