# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 05:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160517_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='effect',
            name='sheets',
        ),
        migrations.AddField(
            model_name='effect',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='effect',
            name='sheet',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Sheet'),
        ),
    ]
