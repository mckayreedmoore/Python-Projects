# Generated by Django 2.2.5 on 2021-02-17 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('state', models.CharField(choices=[('New York', 'NY'), ('Missouri', 'MO'), ('California', 'CA'), ('Washington', 'WA'), ('Michigan', 'MI'), ('Pennsylvania', 'PA')], max_length=10)),
                ('miles', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=10)),
                ('camping', models.BooleanField()),
            ],
        ),
    ]
