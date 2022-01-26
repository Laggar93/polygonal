# Generated by Django 3.2.4 on 2022-01-20 09:41

import advice.models
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('advice', '0015_auto_20220120_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice_blocks',
            name='slide_picture_2_xxl2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2400, 1800], upload_to=advice.models.get_file_path, verbose_name='Изображение 2 для слайдера'),
        ),
        migrations.AlterField(
            model_name='advice_blocks',
            name='slide_picture_3_xxl2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2400, 1800], upload_to=advice.models.get_file_path, verbose_name='Изображение 3 для слайдера'),
        ),
        migrations.AlterField(
            model_name='advice_blocks',
            name='slide_picture_4_xxl2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2400, 1800], upload_to=advice.models.get_file_path, verbose_name='Изображение 4 для слайдера'),
        ),
        migrations.AlterField(
            model_name='advice_blocks',
            name='slide_picture_5_xxl2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2400, 1800], upload_to=advice.models.get_file_path, verbose_name='Изображение 5 для слайдера'),
        ),
        migrations.AlterField(
            model_name='advice_blocks',
            name='slide_picture_6_xxl2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2400, 1800], upload_to=advice.models.get_file_path, verbose_name='Изображение 6 для слайдера'),
        ),
        migrations.AlterField(
            model_name='advice_blocks',
            name='slide_picture_7_xxl2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2400, 1800], upload_to=advice.models.get_file_path, verbose_name='Изображение 7 для слайдера'),
        ),
    ]