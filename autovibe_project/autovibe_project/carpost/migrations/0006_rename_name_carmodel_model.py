# Generated by Django 5.0.3 on 2024-03-13 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpost', '0005_alter_carmodel_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='name',
            new_name='model',
        ),
    ]
