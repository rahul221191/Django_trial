# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
