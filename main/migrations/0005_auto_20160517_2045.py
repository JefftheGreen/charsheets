# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160517_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effect',
            name='parent_effect',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_effect', to='main.Effect'),
        ),
    ]
