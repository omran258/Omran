# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-22 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0106_fill_difficulties'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='last_answer_for_difficulty',
        ),
        migrations.AlterField(
            model_name='difficulty',
            name='lower_limit',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='difficulty',
            name='upper_limit',
            field=models.PositiveIntegerField(),
        ),
    ]
