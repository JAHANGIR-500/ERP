# Generated by Django 5.2.1 on 2025-07-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_receive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcereceive',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
