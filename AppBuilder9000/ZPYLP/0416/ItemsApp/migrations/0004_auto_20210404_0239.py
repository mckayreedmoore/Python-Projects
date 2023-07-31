# Generated by Django 2.2.5 on 2021-04-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemsApp', '0003_auto_20210402_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('Melee', 'Melee'), ('Ranged', 'Ranged'), ('Magic', 'Magic')], default='', max_length=20),
        ),
    ]
