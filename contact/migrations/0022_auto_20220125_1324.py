# Generated by Django 3.2.4 on 2022-01-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0021_auto_20220124_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_main',
            name='intro_title',
            field=models.CharField(blank=True, max_length=500, verbose_name='Приходите в гости'),
        ),
        migrations.AlterField(
            model_name='contact_main',
            name='intro_title_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Приходите в гости'),
        ),
        migrations.AlterField(
            model_name='contact_main',
            name='intro_title_fr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Приходите в гости'),
        ),
        migrations.AlterField(
            model_name='contact_main',
            name='intro_title_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Приходите в гости'),
        ),
        migrations.AlterField(
            model_name='contact_social_networks',
            name='social_network_type',
            field=models.CharField(blank=True, choices=[('1', 'WhatsApp'), ('2', 'Telegram'), ('3', 'Behance'), ('4', 'Facebook'), ('5', 'В Контакте'), ('6', 'Instagram'), ('7', 'YouTube')], max_length=100, unique=True, verbose_name='Тип социальной сети'),
        ),
    ]
