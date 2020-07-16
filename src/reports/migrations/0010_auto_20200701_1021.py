# Generated by Django 3.0.7 on 2020-07-01 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_auto_20200701_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyreport',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='dailyreport',
            name='area',
        ),
        migrations.RemoveField(
            model_name='dailyreport',
            name='cp',
        ),
        migrations.RemoveField(
            model_name='dailyreport',
            name='description',
        ),
        migrations.RemoveField(
            model_name='dailyreport',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='dailyreport',
            name='tag',
        ),
        migrations.CreateModel(
            name='ReportActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('remarks', models.TextField(blank=True)),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reports.Activity')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reports.Area')),
                ('cp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reports.Cp')),
                ('reportnumber', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reports.DailyReport')),
            ],
        ),
    ]