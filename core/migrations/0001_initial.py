# Generated by Django 5.0.4 on 2024-04-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('icon', models.CharField(max_length=225)),
            ],
        ),
    ]
