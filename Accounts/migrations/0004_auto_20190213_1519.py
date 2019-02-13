# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-02-13 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20190213_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pgcorp_user',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'House Owner'), (2, 'Paying Guest')]),
        ),
    ]
