# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-03 03:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0102_fill_revision_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duplicate',
            name='container',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.DuplicateContainer'),
        ),
        migrations.AlterField(
            model_name='duplicatecontainer',
            name='reviser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='exam',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exams', to='exams.Category'),
        ),
        migrations.AlterField(
            model_name='examdate',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exam_dates', to='accounts.Level'),
        ),
        migrations.AlterField(
            model_name='explanationrevision',
            name='submitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submitted_explanations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mnemonic',
            name='submitter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='revision',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_revision', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='revision',
            name='submitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='session',
            name='parent_session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='exams.Session'),
        ),
        migrations.AlterField(
            model_name='source',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.Category'),
        ),
        migrations.AlterField(
            model_name='source',
            name='parent_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='exams.Source'),
        ),
        migrations.AlterField(
            model_name='suggestedchange',
            name='reviser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
