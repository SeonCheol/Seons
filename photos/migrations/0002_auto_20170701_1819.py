# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-01 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='filtered_image',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/filtered'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/orig'),
        ),
    ]
