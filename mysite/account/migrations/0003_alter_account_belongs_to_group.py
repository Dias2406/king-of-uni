# Generated by Django 3.2.12 on 2022-03-14 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('account', '0002_auto_20220301_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='belongs_to_group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='group.group'),
        ),
    ]