# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-22 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DisStatus', '0023_auto_20180521_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailystatusauto',
            name='Remarks',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='dailystatuspq',
            name='Remarks',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='dailystatusqc',
            name='Remarks',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='projectauto',
            name='Remarks',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='projectpq',
            name='Remarks',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='projectqc',
            name='Remarks',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
