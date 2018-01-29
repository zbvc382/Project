# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-29 20:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_requested', models.DateTimeField(auto_now_add=True, null=True)),
                ('leave_type', models.CharField(choices=[('Holiday', 'Holiday'), ('Sick Leave', 'Sick Leave')], default='Holiday', max_length=10)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('reason', models.TextField(max_length=200)),
                ('status', models.CharField(default='pending', max_length=10)),
                ('attachment', models.FileField(blank=True, null=True, upload_to=home.models.user_directory_path)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
