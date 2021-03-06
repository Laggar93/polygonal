# Generated by Django 3.2.4 on 2022-01-17 13:25

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import order_projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(blank=True, max_length=1000, verbose_name='Ключевые слова')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Описание')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('name', models.CharField(max_length=500, verbose_name='Название раздела')),
                ('text', ckeditor.fields.RichTextField(blank=True, verbose_name='Текст после названия')),
            ],
            options={
                'verbose_name': 'Проекты на заказ',
                'verbose_name_plural': 'Проекты на заказ',
            },
        ),
        migrations.CreateModel(
            name='project_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Порядок показа')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать на сайте')),
                ('name', models.CharField(max_length=500, verbose_name='Название проекта')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_project', to='order_projects.project_page', verbose_name='Проекты на заказ')),
            ],
            options={
                'verbose_name': 'Список проектов',
                'verbose_name_plural': 'Списки проектов',
            },
        ),
        migrations.CreateModel(
            name='project_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Порядок показа')),
                ('main_photo_1', models.ImageField(blank=True, null=True, upload_to=order_projects.models.get_file_path)),
                ('main_photo_2', models.ImageField(blank=True, null=True, upload_to=order_projects.models.get_file_path)),
                ('main_photo_3', models.ImageField(blank=True, null=True, upload_to=order_projects.models.get_file_path)),
                ('main_photo_4', models.ImageField(blank=True, null=True, upload_to=order_projects.models.get_file_path)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_project_lists', to='order_projects.project_page', verbose_name='Проекты на заказ')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'ordering': ['order'],
            },
        ),
    ]
