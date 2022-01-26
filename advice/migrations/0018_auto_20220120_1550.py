# Generated by Django 3.2.4 on 2022-01-20 12:50

import advice.models
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('advice', '0017_auto_20220120_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_8_original',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_8_xs',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_8_xs2x',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_8_xxl',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='slide_picture_8_xxl2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2400, 1800], upload_to=advice.models.get_file_path, verbose_name='Изображение 8 для слайдера'),
        ),
    ]