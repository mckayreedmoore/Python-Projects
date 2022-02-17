# Generated by Django 4.0.2 on 2022-02-17 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')], default='none', max_length=10),
        ),
    ]