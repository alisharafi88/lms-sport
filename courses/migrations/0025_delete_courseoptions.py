# Generated by Django 4.2.15 on 2024-09-04 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_remove_course_options_course_analysis_room_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseOptions',
        ),
    ]
