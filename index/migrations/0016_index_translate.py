# Generated by Django 3.2.4 on 2022-01-30 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_auto_20220130_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='index_translate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog', models.CharField(blank=True, max_length=255, null=True, verbose_name='Смотреть в каталог')),
                ('shop', models.CharField(blank=True, max_length=255, null=True, verbose_name='Перейти в магазин')),
            ],
            options={
                'verbose_name': 'Переводы на главной странице',
                'verbose_name_plural': 'Переводы на главной странице',
            },
        ),
    ]
