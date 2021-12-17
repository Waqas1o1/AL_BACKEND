# Generated by Django 3.1.12 on 2021-12-11 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('POS_APP', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='created',
        ),
        migrations.AddField(
            model_name='party',
            name='current_Balance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='party',
            name='opening_Balance',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]