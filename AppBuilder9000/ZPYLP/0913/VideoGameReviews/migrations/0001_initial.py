# Generated by Django 2.2.5 on 2021-08-26 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer', models.CharField(max_length=100)),
                ('game', models.CharField(max_length=100)),
                ('developer', models.CharField(max_length=100)),
                ('review_score', models.DecimalField(decimal_places=1, max_digits=2)),
                ('summary', models.TextField(default='', max_length=500)),
            ],
        ),
    ]
