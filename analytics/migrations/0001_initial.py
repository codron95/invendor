# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-29 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tripData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accx', models.FloatField(default=0)),
                ('accy', models.FloatField(default=0)),
                ('accz', models.FloatField(default=0)),
                ('latd', models.FloatField(default=0)),
                ('longtd', models.FloatField(default=0)),
                ('speed', models.FloatField(default=0)),
                ('speed_limit', models.FloatField(default=0)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
