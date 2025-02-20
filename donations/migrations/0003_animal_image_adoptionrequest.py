# Generated by Django 5.1.6 on 2025-02-17 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_rename_description_animal_help_needed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='animal_images/'),
        ),
        migrations.CreateModel(
            name='AdoptionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adopter_name', models.CharField(max_length=100)),
                ('adopter_email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.animal')),
            ],
        ),
    ]
