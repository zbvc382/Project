# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-03 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20180218_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='comment',
            field=models.TextField(default='', max_length=200),
        ),
    ]