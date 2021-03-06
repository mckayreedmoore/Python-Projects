# Generated by Django 2.2.5 on 2021-04-14 19:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyThai', '0006_auto_20210413_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dishType',
            field=models.CharField(choices=[('Curry', 'Curry'), ('Noodles', 'Noodles'), ('Soup', 'Soup'), ('Appetizers', 'Appetizers'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='dish',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
