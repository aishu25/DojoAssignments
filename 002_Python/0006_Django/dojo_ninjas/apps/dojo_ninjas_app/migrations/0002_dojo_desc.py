# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-25 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default="default_text"),
            preserve_default=False,
        ),
    ]
