# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DisStatus', '0018_auto_20180521_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='logging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=30, null=True)),
                ('action', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
