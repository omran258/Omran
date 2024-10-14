# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 14:49
from __future__ import unicode_literals

from django.db import migrations
from django.db.models import Count

def fill_is_approved(apps, schema_editor):
    Question = apps.get_model('exams', 'Question')
    Question.objects.exclude(issues__is_blocker=True)\
                    .filter(is_deleted=False,
                            best_revision__is_approved=True)\
                    .annotate(choice_count=Count('best_revision__choice'))\
                    .filter(choice_count__gt=1)\
                    .filter(best_revision__choice__is_right=True)\
                    .update(is_approved=True)

def empty_is_approved(apps, schema_editor):
    Question = apps.get_model('exams', 'Question')
    Question.objects.update(is_approved=False)

class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0077_question_is_approved'),
    ]

    operations = [
        migrations.RunPython(fill_is_approved,
                             reverse_code=empty_is_approved)
    ]
