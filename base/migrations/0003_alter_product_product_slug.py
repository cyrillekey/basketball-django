# Generated by Django 3.2.7 on 2021-09-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_product_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
