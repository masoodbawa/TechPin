# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20161019_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name_fa',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Persian Name'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=50, verbose_name='English Name'),
        ),
    ]
