# Generated by Django 2.2.5 on 2021-02-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookClubApp', '0006_auto_20210225_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='read',
            field=models.BooleanField(null=True),
        ),
    ]
