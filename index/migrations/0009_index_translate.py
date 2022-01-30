# Generated by Django 3.2.4 on 2022-01-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20220127_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='index_translate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog', models.CharField(blank=True, max_length=255, null=True, verbose_name='Смотреть каталог')),
                ('catalog_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Смотреть каталог')),
                ('catalog_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Смотреть каталог')),
                ('catalog_fr', models.CharField(blank=True, max_length=255, null=True, verbose_name='Смотреть каталог')),
                ('shop', models.CharField(blank=True, max_length=255, null=True, verbose_name='Перейти в магазин')),
                ('shop_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Перейти в магазин')),
                ('shop_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Перейти в магазин')),
                ('shop_fr', models.CharField(blank=True, max_length=255, null=True, verbose_name='Перейти в магазин')),
            ],
            options={
                'verbose_name': 'Переводы на главной странице',
                'verbose_name_plural': 'Переводы на главной странице',
            },
        ),
    ]
