# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DisStatus', '0003_auto_20180503_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailystatus',
            name='ReleaseVersion',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
