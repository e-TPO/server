# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-27 09:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0002_auto_20180127_0930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placementsessionregistration',
            old_name='current_status',
            new_name='currentStatus',
        ),
    ]