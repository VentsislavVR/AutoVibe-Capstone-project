# Generated by Django 5.0.3 on 2024-03-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carbrand',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='carbrand',
            name='logo',
            field=models.URLField(max_length=220),
        ),
    ]
