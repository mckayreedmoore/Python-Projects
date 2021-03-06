# Generated by Django 2.2.5 on 2021-04-16 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuitarReviewsApp', '0003_auto_20210410_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitarinfo',
            name='brand',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='guitarinfo',
            name='model',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='guitarinfo',
            name='type',
            field=models.CharField(choices=[('Acoustic', 'Acoustic'), ('Electro-Acoustic', 'Electro-Acoustic'), ('Electric', 'Electric'), ('Bass', 'Bass')], max_length=50),
        ),
    ]
