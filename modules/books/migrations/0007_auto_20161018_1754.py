# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-18 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20161016_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_images',
            field=models.ImageField(default='/home/hunter/Desktop/lendMyBookDevf/lendmybook/media/default_images/default_cover.png', upload_to='/home/hunter/Desktop/lendMyBookDevf/lendmybook/media/book_images/'),
        ),
    ]
