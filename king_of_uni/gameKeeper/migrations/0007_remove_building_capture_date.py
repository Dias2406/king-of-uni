# Generated by Django 4.0.1 on 2022-03-22 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameKeeper', '0006_building_capture_date2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='capture_date',
        ),
    ]