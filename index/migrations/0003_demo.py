# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-13 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='-1', max_length=255)),
            ],
        ),
    ]
