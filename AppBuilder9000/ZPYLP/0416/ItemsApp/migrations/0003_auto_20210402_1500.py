# Generated by Django 2.2.5 on 2021-04-02 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemsApp', '0002_auto_20210330_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.URLField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='slot',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(default='', max_length=20),
        ),
    ]
