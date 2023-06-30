# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-26 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_auto_20200226_1335"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="price",),
        migrations.AddField(
            model_name="product",
            name="currency",
            field=models.CharField(default="EUR", max_length=3),
        ),
    ]