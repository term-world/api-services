# Generated by Django 5.0.6 on 2024-06-02 16:07

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransientModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
            },
            managers=[
                ('obj', django.db.models.manager.Manager()),
            ],
        ),
    ]
