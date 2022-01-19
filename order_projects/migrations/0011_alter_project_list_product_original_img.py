# Generated by Django 3.2.4 on 2022-01-18 10:20

from django.db import migrations
import django_resized.forms
import order_projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('order_projects', '0010_rename_main_photo_1_project_images_product_original_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_list',
            name='product_original_img',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[1600, 1200], upload_to=order_projects.models.get_file_path, verbose_name='Основное изображение'),
        ),
    ]