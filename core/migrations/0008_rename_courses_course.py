# Generated by Django 5.0.4 on 2024-04-12 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_courses_image_courses_programs_training_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
    ]