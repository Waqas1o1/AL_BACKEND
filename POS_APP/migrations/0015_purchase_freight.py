# Generated by Django 3.1.12 on 2022-01-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS_APP', '0014_auto_20220115_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='freight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
