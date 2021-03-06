# Generated by Django 2.2.5 on 2021-11-18 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TheForce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jedi', models.CharField(choices=[('Darth Vader', 'Darth Vader'), ('Luke Skywalker', 'Luke Skywalker'), ('Obi-Wan Kenobi', 'Obi_Wan Kenobi'), ('Kylo Ren', 'Kylo Ren')], max_length=25)),
                ('Your_Name', models.CharField(blank=True, default='', max_length=25)),
                ('Your_favorite_movie', models.CharField(blank=True, default='', max_length=25)),
                ('Your_Favorite_Scene', models.CharField(blank=True, default='', max_length=25)),
                ('Light_or_Dark', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('Is_The_Force_With_You', models.TextField(blank=True, default='', max_length=500)),
            ],
        ),
    ]
