# Generated by Django 5.2.1 on 2025-06-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_of_task', models.CharField(max_length=255)),
                ('group_of_task', models.CharField(max_length=255)),
            ],
        ),
    ]
