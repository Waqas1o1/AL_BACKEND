# Generated by Django 3.1.12 on 2022-01-15 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS_APP', '0013_auto_20220115_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='vender',
            name='current_Balance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vender',
            name='opening_Balance',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]