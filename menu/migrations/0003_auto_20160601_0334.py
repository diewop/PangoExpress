# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20160601_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]