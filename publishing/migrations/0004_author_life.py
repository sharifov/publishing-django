# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0003_auto_20151226_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='life',
            field=models.TextField(blank=True, null=True),
        ),
    ]
