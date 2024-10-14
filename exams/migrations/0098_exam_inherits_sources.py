# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-02-12 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0097_exam_m2m_allowed_to_take'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='inherits_sources',
            field=models.BooleanField(default=True, verbose_name='This exam inherits sources from its parent categories'),
        ),
    ]
