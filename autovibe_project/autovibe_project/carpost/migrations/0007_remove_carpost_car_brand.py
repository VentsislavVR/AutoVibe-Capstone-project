# Generated by Django 5.0.3 on 2024-03-13 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpost', '0006_rename_name_carmodel_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carpost',
            name='car_brand',
        ),
    ]
