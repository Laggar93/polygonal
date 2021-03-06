# Generated by Django 3.2.4 on 2022-01-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(blank=True, max_length=1000, verbose_name='Ключевые слова')),
                ('keywords_ru', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ключевые слова')),
                ('keywords_en', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ключевые слова')),
                ('keywords_fr', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ключевые слова')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Описание')),
                ('description_ru', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('description_en', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('description_fr', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='Заголовок')),
                ('title_ru', models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок')),
                ('title_fr', models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название в меню')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Название в меню')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Название в меню')),
                ('name_fr', models.CharField(max_length=255, null=True, verbose_name='Название в меню')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Заголовок страницы')),
                ('text_ru', models.TextField(blank=True, null=True, verbose_name='Заголовок страницы')),
                ('text_en', models.TextField(blank=True, null=True, verbose_name='Заголовок страницы')),
                ('text_fr', models.TextField(blank=True, null=True, verbose_name='Заголовок страницы')),
            ],
            options={
                'verbose_name': 'Правила пользования',
                'verbose_name_plural': 'Правила пользования',
            },
        ),
    ]
