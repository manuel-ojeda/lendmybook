# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-16 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20161016_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_user',
            field=models.AutoField(primary_key=True),
        ),
    ]