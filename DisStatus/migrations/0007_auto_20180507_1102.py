# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 05:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DisStatus', '0006_auto_20180507_1047'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DailyStatus',
            new_name='DailyStatusQC',
        ),
    ]
