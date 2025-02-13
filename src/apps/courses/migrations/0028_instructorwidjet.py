# Generated by Django 4.2.15 on 2024-09-08 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0027_instructor_instagram_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructorWidjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widjet', models.CharField(help_text='short Widjet', max_length=20)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='widjets', to='courses.instructor', verbose_name='instructor widjet')),
            ],
        ),
    ]
