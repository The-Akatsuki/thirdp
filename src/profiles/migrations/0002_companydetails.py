# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 03:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtools', '0003_auto_20160128_0912'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='companyDetails',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]