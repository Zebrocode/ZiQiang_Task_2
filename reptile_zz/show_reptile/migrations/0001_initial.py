# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-15 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=15000)),
            ],
        ),
    ]
