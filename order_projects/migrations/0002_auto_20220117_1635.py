# Generated by Django 3.2.4 on 2022-01-17 13:35

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_list',
            name='is_active_en',
            field=models.BooleanField(default=True, verbose_name='Показывать на сайте'),
        ),
        migrations.AddField(
            model_name='project_list',
            name='is_active_fr',
            field=models.BooleanField(default=True, verbose_name='Показывать на сайте'),
        ),
        migrations.AddField(
            model_name='project_list',
            name='is_active_ru',
            field=models.BooleanField(default=True, verbose_name='Показывать на сайте'),
        ),
        migrations.AddField(
            model_name='project_list',
            name='name_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Название проекта'),
        ),
        migrations.AddField(
            model_name='project_list',
            name='name_fr',
            field=models.CharField(max_length=500, null=True, verbose_name='Название проекта'),
        ),
        migrations.AddField(
            model_name='project_list',
            name='name_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Название проекта'),
        ),
        migrations.AddField(
            model_name='project_list',
            name='project_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_project', to='order_projects.project_page', verbose_name='Проекты на заказ'),
        ),
        migrations.AddField(
            model_name='project_list',
            name='project_fr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_project', to='order_projects.project_page', verbose_name='Проекты на заказ'),
        ),
        migrations.AddField(
            model_name='project_list',
            name='project_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_project', to='order_projects.project_page', verbose_name='Проекты на заказ'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='description_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='description_fr',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='description_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='keywords_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='keywords_fr',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='keywords_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='name_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Название раздела'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='name_fr',
            field=models.CharField(max_length=500, null=True, verbose_name='Название раздела'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='name_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Название раздела'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст после названия'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='text_fr',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст после названия'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст после названия'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='title_fr',
            field=models.CharField(max_length=500, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='project_page',
            name='title_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Заголовок'),
        ),
    ]
