# Generated by Django 3.2.4 on 2022-01-30 17:39

import django.core.validators
from django.db import migrations, models
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_index_translate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index_main',
            name='model_file',
            field=models.FileField(blank=True, help_text='Формат файла: pdf. Ограничение размера: 1 Мбайт.', upload_to=index.models.get_file_path, validators=[django.core.validators.FileExtensionValidator(['pdf', 'zip'])], verbose_name='Файл модели'),
        ),
    ]