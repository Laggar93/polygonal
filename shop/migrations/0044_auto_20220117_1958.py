# Generated by Django 3.2.4 on 2022-01-17 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0043_auto_20220117_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_page',
            name='projects',
            field=models.CharField(blank=True, max_length=255, verbose_name='Проекты на заказ'),
        ),
        migrations.AddField(
            model_name='shop_page',
            name='projects_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Проекты на заказ'),
        ),
        migrations.AddField(
            model_name='shop_page',
            name='projects_fr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Проекты на заказ'),
        ),
        migrations.AddField(
            model_name='shop_page',
            name='projects_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Проекты на заказ'),
        ),
    ]