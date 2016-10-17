# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-16 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='id_user',
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default='1998-01-01'),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='id_facebook',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('id_user','email',)]),
        ),
    ]