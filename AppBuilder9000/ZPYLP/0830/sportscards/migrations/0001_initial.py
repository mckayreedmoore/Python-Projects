# Generated by Django 2.2.5 on 2021-08-11 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Player', models.CharField(default='', max_length=70)),
                ('Year', models.IntegerField(default='', max_length=50)),
                ('Team', models.CharField(default='', max_length=50)),
                ('Brand', models.CharField(default='', max_length=750)),
            ],
        ),
    ]
