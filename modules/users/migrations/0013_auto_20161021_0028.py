# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-21 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20161021_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_facebook',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_user',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]