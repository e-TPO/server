# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-27 10:06
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0005_auto_20180127_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placementsessionregistration',
            name='currentStatus',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
