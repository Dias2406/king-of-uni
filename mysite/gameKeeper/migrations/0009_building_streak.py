# Generated by Django 4.0.1 on 2022-03-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameKeeper', '0008_rename_capture_date2_building_capture_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='streak',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=1),
        ),
    ]