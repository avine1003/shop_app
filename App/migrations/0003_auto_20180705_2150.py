# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-05 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_usermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='u_password',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='_password',
            field=models.CharField(db_column='u_password', max_length=256, null=True),
        ),
    ]
