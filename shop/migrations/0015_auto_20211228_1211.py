# Generated by Django 3.2.4 on 2021-12-28 09:11

from django.db import migrations
import django_resized.forms
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20211223_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='bottom_photo_xxl2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, quality=80, size=[3200, 2400], upload_to=shop.models.get_file_path, verbose_name='Картинка для нижнего блока'),
        ),
        migrations.AlterField(
            model_name='item_photos',
            name='main_photo_xxl2',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, quality=80, size=[3200, 2400], upload_to=shop.models.get_file_path, verbose_name='Картинка'),
        ),
    ]
