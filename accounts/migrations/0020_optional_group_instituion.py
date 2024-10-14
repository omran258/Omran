# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-14 05:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_group_level_relationships'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Institution'),
        ),
    ]
