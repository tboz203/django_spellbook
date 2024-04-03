# Generated by Django 5.0.3 on 2024-04-03 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000, unique=True)),
                ('level', models.IntegerField(default=-1)),
                ('casting_time', models.CharField(max_length=1000)),
                ('range', models.CharField(max_length=1000)),
                ('components', models.CharField(max_length=1000)),
                ('duration', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=5000)),
                ('description_high', models.TextField(max_length=1000)),
                ('book', models.CharField(max_length=50)),
                ('favorite', models.BooleanField(null=True)),
                ('notes', models.TextField(blank=True)),
                ('clases', models.CharField(max_length=300)),
                ('ritual', models.BooleanField()),
                ('concentration', models.BooleanField()),
                ('sound', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
            },
        ),
    ]