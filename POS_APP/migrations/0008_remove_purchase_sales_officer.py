# Generated by Django 3.1.12 on 2022-01-01 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POS_APP', '0007_salesofficer_cnic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='sales_officer',
        ),
    ]
