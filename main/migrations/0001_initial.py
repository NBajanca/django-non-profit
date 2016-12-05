# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 17:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('mobile_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Mobile phone number')),
                ('address', models.CharField(blank=True, help_text='address_help_text', max_length=120, verbose_name='Address')),
                ('academic_qualifications', models.CharField(blank=True, max_length=80, verbose_name='Academic qualifications')),
                ('profession', models.CharField(blank=True, max_length=80, verbose_name='Profession')),
                ('volunteer_experience', models.TextField(blank=True, verbose_name='Volunteer Experience')),
                ('observations', models.TextField(blank=True, verbose_name='Observations')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilizador')),
            ],
        ),
    ]