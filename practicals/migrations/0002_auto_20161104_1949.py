# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-04 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practicals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practical',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
