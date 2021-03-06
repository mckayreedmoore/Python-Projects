# Generated by Django 2.2.5 on 2021-07-28 19:47

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=75, unique=True)),
                ('location', models.CharField(choices=[('Hillsboro', 'Hillsboro'), ('North', 'North'), ('Northeast', 'Northeast'), ('Beaverton', 'Beaverton'), ('Southeast', 'Southeast'), ('Northwest', 'Northwest'), ('Southwest', 'Southwest')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('commute', models.CharField(choices=[('Short', 'Short'), ('Long', 'Long'), ('Fair', 'Fair')], max_length=40)),
                ('walkability', models.CharField(choices=[('Not Walkable', 'Not Walkable'), ('Very Walkable', 'Very Walkable'), ('Somewhat Walkable', 'Somewhat Walkable')], max_length=40)),
                ('reviewer_life_stage', models.CharField(choices=[('Family', 'Family'), ('Retiree', 'Retiree'), ('Young Professional', 'Young Professional')], max_length=40)),
                ('comment', models.CharField(max_length=750)),
                ('neighborhood_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NeighborhoodReview.Neighborhood')),
            ],
            managers=[
                ('Reviews', django.db.models.manager.Manager()),
            ],
        ),
    ]
