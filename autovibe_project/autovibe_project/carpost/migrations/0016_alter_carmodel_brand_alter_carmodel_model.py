# Generated by Django 5.0.3 on 2024-04-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpost', '0015_alter_carfeatures_exterior_features_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(default='Pick a brand', max_length=100),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='model',
            field=models.CharField(default='Pick a model', max_length=100),
        ),
    ]