# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-11 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_session_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_editor',
            field=models.BooleanField(default=False),
        ),
    ]
