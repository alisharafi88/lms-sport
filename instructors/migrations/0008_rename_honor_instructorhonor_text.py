# Generated by Django 4.2.15 on 2024-09-09 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0007_instructorhonor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructorhonor',
            old_name='honor',
            new_name='text',
        ),
    ]
