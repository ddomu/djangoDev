# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-19 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f5app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f5arp',
            name='arp_mac',
            field=models.CharField(max_length=20),
        ),
    ]