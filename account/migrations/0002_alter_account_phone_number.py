# Generated by Django 3.2.7 on 2021-09-14 16:23

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[account.models.TestNumber], verbose_name='phone_number'),
        ),
    ]
