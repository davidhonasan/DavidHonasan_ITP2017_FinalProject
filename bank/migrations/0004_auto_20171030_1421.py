# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20171030_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='user_destination',
            field=models.CharField(max_length=20),
        ),
    ]
