# Generated by Django 3.2.4 on 2022-01-19 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advice', '0002_auto_20220119_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice_main',
            name='advice',
            field=models.CharField(blank=True, max_length=255, verbose_name='Стат. перевод - Советы по сборке'),
        ),
        migrations.AddField(
            model_name='advice_main',
            name='advice_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Стат. перевод - Советы по сборке'),
        ),
        migrations.AddField(
            model_name='advice_main',
            name='advice_fr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Стат. перевод - Советы по сборке'),
        ),
        migrations.AddField(
            model_name='advice_main',
            name='advice_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Стат. перевод - Советы по сборке'),
        ),
    ]