# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-01 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20170701_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='title',
        ),
        migrations.AddField(
            model_name='photo',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
