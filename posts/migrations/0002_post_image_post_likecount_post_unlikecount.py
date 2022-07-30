# Generated by Django 4.0.3 on 2022-03-31 03:55

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='post',
            name='likecount',
            field=models.IntegerField(blank=True, default=0, verbose_name='like_count'),
        ),
        migrations.AddField(
            model_name='post',
            name='unlikecount',
            field=models.IntegerField(blank=True, default=0, verbose_name='unlike_count'),
        ),
    ]
