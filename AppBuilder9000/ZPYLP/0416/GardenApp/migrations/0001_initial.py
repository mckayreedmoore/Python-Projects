# Generated by Django 2.2.5 on 2021-03-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=25)),
                ('name', models.CharField(blank=True, default='', max_length=25)),
            ],
        ),
    ]
