# Generated by Django 3.2.4 on 2022-01-19 18:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advice', '0007_auto_20220119_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advice_blocks',
            name='text',
        ),
        migrations.RemoveField(
            model_name='advice_blocks',
            name='text_en',
        ),
        migrations.RemoveField(
            model_name='advice_blocks',
            name='text_fr',
        ),
        migrations.RemoveField(
            model_name='advice_blocks',
            name='text_ru',
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='bottom_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Нижний текст'),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='bottom_text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Нижний текст'),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='bottom_text_fr',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Нижний текст'),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='bottom_text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Нижний текст'),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='top_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Верхний текст'),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='top_text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Верхний текст'),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='top_text_fr',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Верхний текст'),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='top_text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Верхний текст'),
        ),
    ]