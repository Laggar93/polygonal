# Generated by Django 3.2.4 on 2022-01-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_auto_20220121_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery_main',
            name='master_logo',
            field=models.BooleanField(default=True, verbose_name='Master Card'),
        ),
        migrations.AlterField(
            model_name='delivery_main',
            name='mir_logo',
            field=models.BooleanField(default=True, verbose_name='МИР'),
        ),
        migrations.AlterField(
            model_name='delivery_main',
            name='paypal_logo',
            field=models.BooleanField(default=True, verbose_name='PayPal'),
        ),
        migrations.AlterField(
            model_name='delivery_main',
            name='terminal_logo',
            field=models.BooleanField(default=True, verbose_name='Terminal'),
        ),
        migrations.AlterField(
            model_name='delivery_main',
            name='visa_logo',
            field=models.BooleanField(default=True, verbose_name='Visa'),
        ),
    ]
