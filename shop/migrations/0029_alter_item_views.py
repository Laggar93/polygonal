# Generated by Django 3.2.7 on 2022-01-07 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_auto_20220106_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='views',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество просмотров товара'),
        ),
    ]
