# Generated by Django 5.2.1 on 2025-06-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_bill', '0002_remove_salesbill_name_of_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesbill',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
