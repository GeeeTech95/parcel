# Generated by Django 4.2.11 on 2024-07-19 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20231001_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='country',
            name='short_name',
            field=models.CharField(max_length=20),
        ),
    ]
