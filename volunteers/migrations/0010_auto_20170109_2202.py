# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 22:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0009_volunteerpresence_volunteerunavailability'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='volunteer',
            options={'permissions': (('can_manage', 'Can manage volunteer'),)},
        ),
    ]
