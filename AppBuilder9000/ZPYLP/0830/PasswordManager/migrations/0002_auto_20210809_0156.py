# Generated by Django 2.2.5 on 2021-08-09 06:56

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('PasswordManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewPassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Per', 'Personal'), ('Wrk', 'Work'), ('Cmb', 'Combo'), ('Otr', 'Other')], max_length=8)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_modified_date', models.DateField(auto_now=True)),
                ('website', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=120)),
                ('username', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60, unique=True)),
                ('favorite', models.BooleanField(default=False)),
            ],
            managers=[
                ('NewPasswords', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='NewPasswords',
        ),
    ]