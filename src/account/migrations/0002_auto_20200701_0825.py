# Generated by Django 3.0.7 on 2020-07-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='pgesco_Id',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='account',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]