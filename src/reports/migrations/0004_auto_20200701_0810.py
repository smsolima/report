# Generated by Django 3.0.7 on 2020-07-01 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_remove_dailyreport_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wind',
            name='wind_velocity',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
