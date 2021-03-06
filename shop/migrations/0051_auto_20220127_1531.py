# Generated by Django 3.2.4 on 2022-01-27 12:31

from django.db import migrations, models
import django_resized.forms
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0050_auto_20220127_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='index_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Текст на главной странице'),
        ),
        migrations.AddField(
            model_name='category',
            name='index_text_fr',
            field=models.TextField(blank=True, null=True, verbose_name='Текст на главной странице'),
        ),
        migrations.AddField(
            model_name='category',
            name='index_text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Текст на главной странице'),
        ),
        migrations.AlterField(
            model_name='category',
            name='index_photo_xs2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2048, 1410], upload_to=shop.models.get_file_path, verbose_name='Картинка на главной странице'),
        ),
    ]
