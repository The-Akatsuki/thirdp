# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_companydetails_lymo_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetails',
            name='userType',
            field=models.CharField(choices=[('company_secretary', 'company Secretary'), ('company_commission', 'Third party travel desk Secretary')], default='company_secretary', max_length=50, verbose_name='user Type'),
        ),
    ]
