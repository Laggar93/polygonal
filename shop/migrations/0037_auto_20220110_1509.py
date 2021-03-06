# Generated by Django 3.2.4 on 2022-01-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0036_auto_20220110_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='ends',
            field=models.DateField(blank=True, null=True, verbose_name='Окончание действия'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='ends_en',
            field=models.DateField(blank=True, null=True, verbose_name='Окончание действия'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='ends_fr',
            field=models.DateField(blank=True, null=True, verbose_name='Окончание действия'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='ends_ru',
            field=models.DateField(blank=True, null=True, verbose_name='Окончание действия'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='starts',
            field=models.DateField(blank=True, null=True, verbose_name='Начало действия'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='starts_en',
            field=models.DateField(blank=True, null=True, verbose_name='Начало действия'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='starts_fr',
            field=models.DateField(blank=True, null=True, verbose_name='Начало действия'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='starts_ru',
            field=models.DateField(blank=True, null=True, verbose_name='Начало действия'),
        ),
    ]
