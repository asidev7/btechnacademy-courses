# Generated by Django 5.0.4 on 2024-04-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('reponses', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
    ]