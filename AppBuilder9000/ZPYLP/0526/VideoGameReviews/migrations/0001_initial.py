# Generated by Django 2.2.5 on 2021-05-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GameName', models.CharField(max_length=60)),
                ('GameGenre', models.CharField(max_length=60)),
                ('GameReview', models.TextField(max_length=700)),
                ('GameRating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
            ],
        ),
    ]
