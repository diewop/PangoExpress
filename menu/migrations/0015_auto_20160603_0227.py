# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 02:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_auto_20160603_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='descripcion',
            field=models.CharField(default='No hay descripcion disponible', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plato',
            name='path_img',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='plato_en_menu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.MENU'),
        ),
    ]