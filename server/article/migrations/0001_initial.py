# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-27 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('body', models.TextField()),
                ('summary', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, max_length=255, null=True)),
                ('url', models.URLField(max_length=255)),
                ('status', models.CharField(choices=[('ADD', 'Added'), ('SUM', 'Summarized'), ('OTH', 'Other')], max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
