# Generated by Django 3.1.12 on 2021-12-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS_APP', '0006_auto_20211212_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesofficer',
            name='cnic',
            field=models.CharField(default=0, max_length=18),
            preserve_default=False,
        ),
    ]
