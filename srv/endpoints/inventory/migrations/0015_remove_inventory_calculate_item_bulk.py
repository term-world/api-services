# Generated by Django 5.0.6 on 2024-06-12 17:04

import pgtrigger.migrations
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_remove_inventory_calculate_item_bulk_and_more'),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name='inventory',
            name='calculate_item_bulk',
        ),
    ]
