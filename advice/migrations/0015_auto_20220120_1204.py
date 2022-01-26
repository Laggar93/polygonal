# Generated by Django 3.2.4 on 2022-01-20 09:04

import advice.models
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('advice', '0014_auto_20220120_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_2_original',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_2_xs',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_2_xs2x',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_2_xxl',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_2_xxl2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2400, 1800], upload_to=advice.models.get_file_path, verbose_name='Изображение 1 для слайдера'),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_3_original',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_3_xs',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_3_xs2x',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_3_xxl',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_3_xxl2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2400, 1800], upload_to=advice.models.get_file_path, verbose_name='Изображение 1 для слайдера'),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_4_original',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_4_xs',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_4_xs2x',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_4_xxl',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_4_xxl2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2400, 1800], upload_to=advice.models.get_file_path, verbose_name='Изображение 1 для слайдера'),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_5_original',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_5_xs',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_5_xs2x',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_5_xxl',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_5_xxl2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2400, 1800], upload_to=advice.models.get_file_path, verbose_name='Изображение 1 для слайдера'),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_6_original',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_6_xs',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_6_xs2x',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_6_xxl',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_6_xxl2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2400, 1800], upload_to=advice.models.get_file_path, verbose_name='Изображение 1 для слайдера'),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_7_original',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_7_xs',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_7_xs2x',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_7_xxl',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_7_xxl2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2400, 1800], upload_to=advice.models.get_file_path, verbose_name='Изображение 1 для слайдера'),
        ),
    ]