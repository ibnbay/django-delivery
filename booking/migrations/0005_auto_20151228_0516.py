# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 22:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20151228_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydelivery',
            name='pickup_time',
            field=models.TimeField(default=datetime.time),
        ),
        migrations.AlterField(
            model_name='companydelivery',
            name='toc_insurance',
            field=models.TextField(),
        ),
    ]
