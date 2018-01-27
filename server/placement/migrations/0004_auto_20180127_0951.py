# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-27 09:51
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0003_auto_20180127_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placementsession',
            name='rounds',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'no': 1, 'rounds_detail': [{'description': 'Sample description', 'step': 1, 'title': 'Sample round detail'}, {'description': 'Sample description', 'step': 1, 'title': 'Sample round detail'}]}),
        ),
        migrations.AlterField(
            model_name='placementsessionregistration',
            name='currentStatus',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'current_status': 1, 'description': 'Hello World'}),
        ),
    ]
