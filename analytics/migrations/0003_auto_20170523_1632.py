# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-23 11:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20170523_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tripanalytics',
            old_name='gyrox',
            new_name='gyroz',
        ),
    ]
