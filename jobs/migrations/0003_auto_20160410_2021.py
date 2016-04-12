# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 20:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_employer_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='state',
        ),
        migrations.AlterField(
            model_name='location',
            name='flagged',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]