# Generated by Django 5.2.1 on 2025-06-26 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design_department', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='designdepartment',
            options={'permissions': [('can_access_design_department', 'Can access Design Department')]},
        ),
        migrations.RenameField(
            model_name='designdepartment',
            old_name='name',
            new_name='title',
        ),
    ]
