# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-22 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default='', max_length=100),
        ),
    ]
