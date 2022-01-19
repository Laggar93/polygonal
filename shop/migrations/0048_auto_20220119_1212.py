# Generated by Django 3.2.4 on 2022-01-19 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0047_shop_page_advice'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_page',
            name='advice_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Советы по сборке'),
        ),
        migrations.AddField(
            model_name='shop_page',
            name='advice_fr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Советы по сборке'),
        ),
        migrations.AddField(
            model_name='shop_page',
            name='advice_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Советы по сборке'),
        ),
    ]
