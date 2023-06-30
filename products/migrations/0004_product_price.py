# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-26 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_auto_20200226_1934"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2, default=1, max_digits=6
            ),
        ),
    ]