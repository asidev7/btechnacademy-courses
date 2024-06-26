# Generated by Django 5.0.4 on 2024-04-12 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_reponses_faq_reponse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('Price', models.PositiveIntegerField(default=0)),
                ('Finance_options', models.CharField(max_length=255)),
                ('Study_method', models.CharField(max_length=255)),
                ('Duration', models.CharField(max_length=255)),
                ('Overview', models.TextField()),
                ('Course_Outline', models.TextField()),
                ('Advantages', models.TextField()),
                ('Requirements', models.TextField()),
                ('Certificates', models.TextField()),
                ('status', models.CharField(choices=[('on_demand', 'On Demand'), ('available', 'Available'), ('coming_soon', 'Coming Soon')], default='available', max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tags')),
            ],
        ),
        migrations.DeleteModel(
            name='Realisation',
        ),
    ]
