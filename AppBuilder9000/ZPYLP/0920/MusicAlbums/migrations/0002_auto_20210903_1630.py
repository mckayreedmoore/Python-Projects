# Generated by Django 2.2.5 on 2021-09-03 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MusicAlbums', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='Name',
            new_name='Album',
        ),
    ]
