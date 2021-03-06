# Generated by Django 2.2.5 on 2021-05-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockTrading', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=10)),
                ('subtitle', models.CharField(blank=True, max_length=10)),
                ('objective', models.TextField(blank=True, max_length=1000)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('tags', models.CharField(blank=True, max_length=50)),
                ('content', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]
