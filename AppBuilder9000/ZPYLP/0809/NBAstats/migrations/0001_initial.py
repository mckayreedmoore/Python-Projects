# Generated by Django 2.2.5 on 2021-07-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Defensive_Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('2020-2021', '2020-2021'), ('2019-2020', '2019-2020'), ('2018-2019', '2018-2019')], max_length=10)),
                ('playerName', models.CharField(max_length=60)),
                ('defRebs', models.IntegerField()),
                ('steals', models.IntegerField()),
                ('blocks', models.IntegerField()),
            ],
        ),
    ]
