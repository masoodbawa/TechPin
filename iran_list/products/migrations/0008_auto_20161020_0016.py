# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='user_type',
            field=models.BooleanField(default=False, verbose_name='Type'),
        ),
    ]