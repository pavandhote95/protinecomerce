# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-20 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("price", models.FloatField()),
                ("image", models.ImageField(upload_to="images")),
                ("category_id", models.IntegerField()),
                ("quantity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
            ],
        ),
    ]