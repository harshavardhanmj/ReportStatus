# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 05:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DisStatus', '0016_auto_20180514_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailystatusauto',
            name='ReleaseVersion',
        ),
        migrations.RemoveField(
            model_name='dailystatuspq',
            name='ReleaseVersion',
        ),
        migrations.RemoveField(
            model_name='dailystatusqc',
            name='ReleaseVersion',
        ),
        migrations.RemoveField(
            model_name='projectauto',
            name='ReleaseVersion',
        ),
        migrations.RemoveField(
            model_name='projectpq',
            name='ReleaseVersion',
        ),
        migrations.RemoveField(
            model_name='projectqc',
            name='ReleaseVersion',
        ),
    ]