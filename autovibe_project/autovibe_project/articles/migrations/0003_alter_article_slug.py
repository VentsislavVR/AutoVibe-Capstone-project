# Generated by Django 5.0.3 on 2024-04-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_description_article_article_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]