# Generated by Django 2.2.5 on 2021-05-24 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockTrading', '0002_resources'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='URL',
            field=models.URLField(blank=True),
        ),
    ]
