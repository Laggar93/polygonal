# Generated by Django 3.2.4 on 2022-01-10 12:47

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0038_auto_20220110_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='main_photo_thumb_xs',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.get_file_path),
        ),
        migrations.AddField(
            model_name='item',
            name='main_photo_thumb_xs2',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.get_file_path),
        ),
    ]
