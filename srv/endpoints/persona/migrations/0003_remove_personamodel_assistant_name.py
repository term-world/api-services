# Generated by Django 5.0.6 on 2024-06-20 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_rename_name_personamodel_assistant_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personamodel',
            name='assistant_name',
        ),
    ]
