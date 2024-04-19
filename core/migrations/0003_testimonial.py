# Generated by Django 5.0.4 on 2024-04-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_services_service_realisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author_name', models.CharField(max_length=100)),
                ('author_title', models.CharField(max_length=100)),
                ('author_image', models.ImageField(upload_to='testimonial_images/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]