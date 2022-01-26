# Generated by Django 3.2.4 on 2022-01-21 11:05

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='delivery_article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Порядок показа')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('intro_text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Вступительный текст')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('bold_text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Жирный текст под таблицей')),
                ('grey_text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Серый текст под таблицей')),
            ],
            options={
                'verbose_name': 'Список статей доставки и оплаты',
                'verbose_name_plural': 'Списки статей доставки и оплаты',
            },
        ),
        migrations.CreateModel(
            name='delivery_columns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_column', models.CharField(blank=True, max_length=500, null=True, verbose_name='Первый столбец')),
                ('second_column', models.CharField(blank=True, max_length=500, null=True, verbose_name='Второй столбец')),
                ('third_column', models.CharField(blank=True, max_length=500, null=True, verbose_name='Третий столбец')),
                ('delivery_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.delivery_article', verbose_name='Списки статей доставки и оплаты')),
            ],
            options={
                'verbose_name': 'Столбец',
                'verbose_name_plural': 'Столбцы',
            },
        ),
    ]