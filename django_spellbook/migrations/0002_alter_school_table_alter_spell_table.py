# Generated by Django 5.0.3 on 2024-04-03 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_spellbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='school',
            table='school',
        ),
        migrations.AlterModelTable(
            name='spell',
            table='spell',
        ),
    ]