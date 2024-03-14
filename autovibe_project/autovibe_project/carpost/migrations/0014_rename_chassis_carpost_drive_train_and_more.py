# Generated by Django 5.0.3 on 2024-03-14 14:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpost', '0013_alter_carpost_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carpost',
            old_name='chassis',
            new_name='drive_train',
        ),
        migrations.AddField(
            model_name='carpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='carbrands',
            name='brand_name',
            field=models.CharField(choices=[('ACURA', 'ACURA'), ('ALFA ROMEO', 'ALFA ROMEO'), ('ASTON MARTIN', 'ASTON MARTIN'), ('AUDI', 'AUDI'), ('BENTLEY', 'BENTLEY'), ('BMW', 'BMW'), ('BUICK', 'BUICK'), ('CADILLAC', 'CADILLAC'), ('CHEVROLET', 'CHEVROLET'), ('CHRYSLER', 'CHRYSLER'), ('DODGE', 'DODGE'), ('FERRARI', 'FERRARI'), ('FIAT', 'FIAT'), ('FORD', 'FORD'), ('GENESIS', 'GENESIS'), ('GMC', 'GMC'), ('HONDA', 'HONDA'), ('HYUNDAI', 'HYUNDAI'), ('INFINITI', 'INFINITI'), ('JAGUAR', 'JAGUAR'), ('JEEP', 'JEEP'), ('KIA', 'KIA'), ('LAMBORGHINI', 'LAMBORGHINI'), ('LAND ROVER', 'LAND ROVER'), ('LEXUS', 'LEXUS'), ('LINCOLN', 'LINCOLN'), ('LOTUS', 'LOTUS'), ('MASERATI', 'MASERATI'), ('MAZDA', 'MAZDA'), ('MCLAREN', 'MCLAREN'), ('MERCEDES-BENZ', 'MERCEDES-BENZ'), ('MINI', 'MINI'), ('MITSUBISHI', 'MITSUBISHI'), ('NISSAN', 'NISSAN'), ('PAGANI', 'PAGANI'), ('PORSCHE', 'PORSCHE'), ('RAM', 'RAM'), ('ROLLS-ROYCE', 'ROLLS-ROYCE'), ('SMART', 'SMART'), ('SUBARU', 'SUBARU'), ('TESLA', 'TESLA'), ('TOYOTA', 'TOYOTA'), ('VOLKSWAGEN', 'VOLKSWAGEN'), ('VOLVO', 'VOLVO')], max_length=100, unique=True),
        ),
    ]