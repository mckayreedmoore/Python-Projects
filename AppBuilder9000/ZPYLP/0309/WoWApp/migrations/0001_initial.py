# Generated by Django 2.2.5 on 2020-12-31 21:23

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Thrall', 'Thrall'), ('Jaina', 'Jaina'), ('Anduin', 'Anduin'), ('Cairne Bloodhoof', 'Cairne Bloodhoof'), ('Tyrande Whisperwind', 'Tyrande Whisperwind'), ('Other', 'Other')], default='', max_length=100, verbose_name='Character name')),
                ('side', models.CharField(choices=[('Alliance', 'Alliance'), ('Horde', 'Horde'), ('Neutral', 'Neutral')], default='', max_length=50, verbose_name='What side are they for the horde, alliance, or neutral?')),
                ('choice', models.CharField(choices=[('Dark', 'Dark'), ('Light', 'Light')], default='', max_length=100, verbose_name='Are they for dark side or light side?')),
                ('powers', models.CharField(max_length=50, verbose_name='Powers')),
                ('bio', models.TextField(verbose_name='Biography')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, verbose_name='Character name')),
                ('description', models.CharField(blank=True, default='', max_length=500, verbose_name='Description')),
                ('path', models.CharField(max_length=100, verbose_name='Path')),
                ('extension', models.CharField(default='', max_length=50, verbose_name='Extension')),
                ('api_id', models.CharField(default='', max_length=50, verbose_name='ID')),
                ('link', models.CharField(blank=True, default=True, max_length=150, verbose_name='Link')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
