# Generated by Django 2.2.5 on 2021-02-18 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HikingFunApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trails',
            name='miles',
        ),
        migrations.RemoveField(
            model_name='trails',
            name='state',
        ),
        migrations.AddField(
            model_name='trails',
            name='location',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='trails',
            name='roundtripMiles',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='trails',
            name='camping',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='trails',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
    ]
