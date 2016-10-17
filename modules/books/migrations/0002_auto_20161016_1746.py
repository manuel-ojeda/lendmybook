# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-16 17:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base_books', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AddField(
            model_name='book',
            name='aditional_info',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='book',
            name='base_book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='base_books.BaseBook'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_images',
            field=models.ImageField(default='../../media/default_images/default_cover.png', upload_to='../../media/book_images/'),
        ),
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='id_book',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]