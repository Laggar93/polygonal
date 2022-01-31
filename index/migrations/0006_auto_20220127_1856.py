# Generated by Django 3.2.4 on 2022-01-27 15:56

from django.db import migrations, models
import django_resized.forms
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_alter_order_point_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_point',
            name='promo_photo_md',
            field=models.ImageField(blank=True, null=True, upload_to=index.models.get_file_path),
        ),
        migrations.AddField(
            model_name='order_point',
            name='promo_photo_md2x',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[2048, 1202], upload_to=index.models.get_file_path, verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='order_point',
            name='promo_photo_xs',
            field=models.ImageField(blank=True, null=True, upload_to=index.models.get_file_path),
        ),
        migrations.AddField(
            model_name='order_point',
            name='promo_photo_xs2x',
            field=models.ImageField(blank=True, null=True, upload_to=index.models.get_file_path),
        ),
    ]