# Generated by Django 2.2.5 on 2021-07-13 16:33

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreciousMetalsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('make', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('price', models.IntegerField()),
                ('form', models.CharField(choices=[('coin', 'coin'), ('bar', 'bar'), ('raw', 'raw')], max_length=10)),
                ('count', models.IntegerField()),
            ],
            managers=[
                ('metals', django.db.models.manager.Manager()),
            ],
        ),
    ]
