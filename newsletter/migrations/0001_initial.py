# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('timestamp', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('updated', models.BooleanField(default=False)),
            ],
        ),
    ]
