# Generated by Django 3.1.2 on 2020-10-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201016_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
