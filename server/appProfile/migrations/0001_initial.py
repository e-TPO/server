# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-25 18:56
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('fcm_token', models.TextField(blank=True, max_length=32)),
                ('roll_no', models.TextField(default=0, max_length=8)),
                ('avatar', models.ImageField(blank=True, upload_to='uploads/avatar/')),
                ('resume', models.FileField(blank=True, upload_to='uploads/resume/')),
                ('social', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('projects', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('achievements', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
