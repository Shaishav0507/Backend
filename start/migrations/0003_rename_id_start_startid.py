# Generated by Django 3.2.10 on 2022-02-22 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0002_alter_start_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='start',
            old_name='id',
            new_name='StartId',
        ),
    ]
