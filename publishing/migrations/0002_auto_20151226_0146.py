# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]