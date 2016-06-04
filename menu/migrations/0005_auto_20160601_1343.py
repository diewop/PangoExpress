# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 13:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20160601_0350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientes',
            old_name='plato_id',
            new_name='plato',
        ),
        migrations.RenameField(
            model_name='ingredientes',
            old_name='producto_id',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='interes_perfil',
            old_name='perfil_id',
            new_name='perfil',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='establecimiento_id',
            new_name='establecimiento',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='producto_id',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='establecimiento_id',
            new_name='establecimiento',
        ),
        migrations.RenameField(
            model_name='ofrece',
            old_name='producto_id',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='establecimiento_id',
            new_name='establecimiento',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='producto_id',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='plato',
            old_name='establecimiento_id',
            new_name='establecimiento',
        ),
        migrations.RenameField(
            model_name='telefonos_restaurant',
            old_name='establecimiento_id',
            new_name='establecimiento',
        ),
        migrations.RenameField(
            model_name='transaccion',
            old_name='billetera_id',
            new_name='billetera',
        ),
        migrations.RenameField(
            model_name='transaccion',
            old_name='establecimiento_id',
            new_name='establecimiento',
        ),
        migrations.AlterUniqueTogether(
            name='ingredientes',
            unique_together=set([('plato', 'producto')]),
        ),
        migrations.AlterUniqueTogether(
            name='inventario',
            unique_together=set([('establecimiento', 'producto')]),
        ),
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together=set([('establecimiento', 'plato')]),
        ),
        migrations.AlterUniqueTogether(
            name='ofrece',
            unique_together=set([('email', 'producto')]),
        ),
        migrations.AlterUniqueTogether(
            name='pedido',
            unique_together=set([('establecimiento', 'producto', 'email')]),
        ),
        migrations.AlterUniqueTogether(
            name='plato',
            unique_together=set([('establecimiento', 'nombre')]),
        ),
        migrations.AlterUniqueTogether(
            name='transaccion',
            unique_together=set([('establecimiento', 'billetera')]),
        ),
    ]