# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 05:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0020_remove_account_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
    ]
