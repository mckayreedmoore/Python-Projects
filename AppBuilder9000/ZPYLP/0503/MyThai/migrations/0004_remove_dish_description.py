# Generated by Django 2.2.5 on 2021-04-13 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyThai', '0003_auto_20210413_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='description',
        ),
    ]
