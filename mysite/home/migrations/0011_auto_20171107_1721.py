# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-07 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20171107_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=home.models.user_directory_path),
        ),
    ]
