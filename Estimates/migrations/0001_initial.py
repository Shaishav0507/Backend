# Generated by Django 3.2.10 on 2022-04-30 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('EstimateId', models.AutoField(primary_key=True, serialize=False)),
                ('EstimateNo', models.CharField(max_length=100, verbose_name='Estimate No.')),
                ('Create', models.CharField(max_length=100, verbose_name='Create')),
                ('Update', models.CharField(max_length=100, verbose_name='Update')),
                ('Item', models.CharField(max_length=50, verbose_name='Item')),
                ('Price', models.CharField(max_length=15, verbose_name='Price')),
            ],
        ),
    ]
