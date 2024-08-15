# Generated by Django 5.0.7 on 2024-07-24 19:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travel',
            name='comfort_rating',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='crowd_rating',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='cultural_sites',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='image',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='location',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='places_to_visit',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='safety_rating',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='vegetation_rating',
        ),
        migrations.AddField(
            model_name='travel',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='travel',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
