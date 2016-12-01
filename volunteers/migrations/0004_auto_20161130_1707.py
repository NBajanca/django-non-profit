# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0003_auto_20161117_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteercomplementarycontact',
            name='volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_complementary_contact_list', to='volunteers.Volunteer'),
        ),
    ]
