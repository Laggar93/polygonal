# Generated by Django 3.2.4 on 2021-10-20 15:04

from django.db import migrations, models
import django_resized.forms
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20211020_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item_photos',
            name='image_1600',
        ),
        migrations.RemoveField(
            model_name='item_photos',
            name='image_800',
        ),
        migrations.AddField(
            model_name='item_photos',
            name='main_photo_popup',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.get_file_path),
        ),
        migrations.AddField(
            model_name='item_photos',
            name='main_photo_xs',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.get_file_path),
        ),
        migrations.AddField(
            model_name='item_photos',
            name='main_photo_xs2',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.get_file_path),
        ),
        migrations.AddField(
            model_name='item_photos',
            name='main_photo_xxl',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.get_file_path),
        ),
        migrations.AddField(
            model_name='item_photos',
            name='main_photo_xxl2',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default=1, force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, quality=80, size=[2400, 1800], upload_to=shop.models.get_file_path, verbose_name='Основное изображение'),
            preserve_default=False,
        ),
    ]
