# Generated by Django 3.2.4 on 2022-03-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0056_auto_20220303_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_page',
            name='total',
            field=models.CharField(blank=True, max_length=255, verbose_name='Итого'),
        ),
        migrations.AddField(
            model_name='shop_page',
            name='total_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Итого'),
        ),
        migrations.AddField(
            model_name='shop_page',
            name='total_fr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Итого'),
        ),
        migrations.AddField(
            model_name='shop_page',
            name='total_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Итого'),
        ),
    ]