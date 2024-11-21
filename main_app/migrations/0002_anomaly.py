# Generated by Django 5.1.3 on 2024-11-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anomaly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('danger_level', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]