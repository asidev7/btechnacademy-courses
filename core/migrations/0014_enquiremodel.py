# Generated by Django 5.0.4 on 2024-04-14 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquireModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('preferred_date_time', models.DateTimeField()),
                ('any_previous_experience_on_IT', models.TextField()),
                ('Any_special_request_accommodations', models.TextField()),
                ('comments_question', models.TextField()),
                ('Select_Course_Certification_Exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course')),
            ],
        ),
    ]
