# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20170830_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=20, null=True, verbose_name='Mobile'),
        ),
    ]
