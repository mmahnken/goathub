# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goat',
            name='photo',
            field=models.ImageField(blank=True, upload_to='goats/media'),
        ),
    ]
