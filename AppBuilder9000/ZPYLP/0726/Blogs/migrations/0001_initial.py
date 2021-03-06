# Generated by Django 2.2.5 on 2021-07-14 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('text', models.TextField(default='')),
                ('date_posted', models.DateTimeField(default='')),
                ('Mood', models.CharField(choices=[('Awesome', 'Awesome'), ('Good', 'Good'), ('Meh', 'Meh'), ('Down', 'Down'), ('Awful', 'Awful'), ('Destructive', 'Destructive')], default='', max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Entries',
            },
        ),
    ]
