# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-27 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('ADD', 'Added'), ('SUM', 'Summarized'), ('OTH', 'Other')], default='ADD', max_length=3),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
