# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-18 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basebook',
            name='cover_image',
            field=models.ImageField(default='/home/hunter/Desktop/lendMyBookDevf/lendmybook/media/default_images/default_cover.png', upload_to='/home/hunter/Desktop/lendMyBookDevf/lendmybook/media/cover_images/'),
        ),
    ]