# Generated by Django 3.2.12 on 2022-03-01 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='belongs_to_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.group'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_inTeam',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='score',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=7),
        ),
    ]