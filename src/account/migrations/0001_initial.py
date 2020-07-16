# Generated by Django 3.0.7 on 2020-06-29 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('firstname', models.CharField(blank=True, max_length=20)),
                ('lastname', models.CharField(blank=True, max_length=20)),
                ('image', models.ImageField(upload_to='accounts/images/')),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(blank=True, max_length=20)),
                ('VoIP', models.CharField(blank=True, max_length=20)),
                ('site', models.CharField(blank=True, max_length=20)),
                ('status', models.BooleanField(default=True)),
                ('Discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Discipline')),
            ],
        ),
    ]