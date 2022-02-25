# Generated by Django 3.2.10 on 2022-02-24 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GST',
            fields=[
                ('GSTId', models.AutoField(primary_key=True, serialize=False)),
                ('Fname', models.CharField(max_length=100, verbose_name='First name')),
                ('Lname', models.CharField(max_length=100, verbose_name='Last name')),
                ('GSTNo', models.CharField(max_length=100, verbose_name='GSTNo')),
                ('Email', models.CharField(max_length=50, verbose_name='Email')),
                ('Phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('Address', models.CharField(max_length=100, verbose_name='Address')),
                ('State', models.CharField(max_length=100, verbose_name='State')),
                ('Code', models.CharField(max_length=6, verbose_name='Code')),
                ('Account', models.CharField(max_length=100, verbose_name='Account')),
            ],
        ),
    ]