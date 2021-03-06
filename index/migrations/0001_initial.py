# Generated by Django 3.2.4 on 2022-01-27 11:48

from django.db import migrations, models
import django_resized.forms
import index.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='index_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(blank=True, max_length=1000, verbose_name='Ключевые слова')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Описание')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='Заголовок')),
                ('title_page', models.CharField(blank=True, max_length=500, verbose_name='Заголовок')),
                ('title_text', models.CharField(blank=True, max_length=500, verbose_name='Приходите в гости')),
                ('main_photo_xl2x', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', keep_meta=True, null=True, quality=80, size=[3840, 1720], upload_to=index.models.get_file_path, verbose_name='Картинка')),
                ('main_photo_xl', models.ImageField(blank=True, null=True, upload_to=index.models.get_file_path)),
                ('main_photo_md', models.ImageField(blank=True, null=True, upload_to=index.models.get_file_path)),
                ('main_photo_md2x', models.ImageField(blank=True, null=True, upload_to=index.models.get_file_path)),
                ('main_photo_sm', models.ImageField(blank=True, null=True, upload_to=index.models.get_file_path)),
                ('main_photo_sm2x', models.ImageField(blank=True, null=True, upload_to=index.models.get_file_path)),
                ('main_photo_xs', models.ImageField(blank=True, null=True, upload_to=index.models.get_file_path)),
                ('main_photo_xs2x', models.ImageField(blank=True, null=True, upload_to=index.models.get_file_path)),
            ],
        ),
    ]
