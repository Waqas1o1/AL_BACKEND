# Generated by Django 3.1.12 on 2022-01-15 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POS_APP', '0012_sales_salesproducts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venderledger',
            old_name='sales_officer',
            new_name='vender',
        ),
    ]
