# Generated by Django 3.2.7 on 2021-10-06 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20211006_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_paid',
            field=models.IntegerField(),
        ),
    ]
